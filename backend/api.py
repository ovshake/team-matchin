from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from playground import get_gpt3_response
import os
import openai
origins = ["*"]
methods = ["*"]
headers = ["*"]



app = FastAPI(
    title="Birdiefy AI Model",
    description="The Birdiefy API for processing a golf swing in video and returning swing info.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to Match[In]!"}

@app.get("/chat", name="Chat Point", summary="Returns the chat bot response")
def get_response(prompt: str):
    try:
        return get_gpt3_response(prompt)
    except openai.error.ServiceUnavailableError:
        return {"error": "OpenAI service unavailable"}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    run(app, host="0.0.0.0", port=port)
