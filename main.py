
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="My First FastAPI Application",
    description="CAIE Course - Assignment 4",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Hello, FastAPI",
        "status": "Application is running successfully"
    }

# Greeting endpoint with path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    return {
        "message": f"Hello, {name}!",
        "course": "CAIE FastAPI Assignment"
    }

# Additional endpoint with query parameter
@app.get("/welcome")
def welcome_user(name: str = "Student"):
    return {
        "message": f"Welcome to FastAPI, {name}!"
    }
