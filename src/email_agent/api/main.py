from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from email_agent.api.routes import router

app = FastAPI(
    title="Enterprise AI Email Agent API",
    description="Backend API for the Enterprise AI Email Agent",
    version="1.0.0",
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Email Agent API is running."
    }