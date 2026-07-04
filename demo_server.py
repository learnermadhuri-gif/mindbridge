#!/usr/bin/env python3
"""Standalone web chat server for the MindBridge demo."""

import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import app as adk_app

app = FastAPI(title="MindBridge Demo")

if not os.environ.get("GOOGLE_API_KEY") and not os.environ.get("GOOGLE_CLOUD_PROJECT"):
    raise RuntimeError(
        "Set GOOGLE_API_KEY or GOOGLE_CLOUD_PROJECT before starting the server."
    )

SESSION_SERVICE = InMemorySessionService()
ARTIFACT_SERVICE = None
runner = Runner(
    app=adk_app,
    session_service=SESSION_SERVICE,
    artifact_service=ARTIFACT_SERVICE,
    auto_create_session=True,
)

FRONTEND_DIR = Path(__file__).parent / "frontend"


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=(FRONTEND_DIR / "index.html").read_text())


@app.post("/run")
async def run(request: Request):
    body = await request.json()
    user_message = body.get("message", "")
    session_id = body.get("session_id") or f"demo_{os.urandom(8).hex()}"
    user_id = "demo_user"

    await SESSION_SERVICE.create_session(
        app_name=adk_app.name,
        user_id=user_id,
        session_id=session_id,
    )

    final_response = ""
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role="user", parts=[types.Part(text=user_message)]
            ),
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        final_response = part.text
    except Exception as e:
        return {"response": "Server error: " + str(e), "session_id": session_id}

    return {"response": final_response, "session_id": session_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
