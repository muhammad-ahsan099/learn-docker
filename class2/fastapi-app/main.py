"""
Sample FastAPI application with two endpoints:
1. GET / - Returns a greeting message.
2. GET /health - Returns the health status of the application.
"""
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def main():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "healthy"}
