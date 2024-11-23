from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, user_routes

# Initialize app
app = FastAPI(
    title="Quiz and Nootes App",
    description="An API fro managing users, notes, quizzes and assignments",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Quiz and Notes App"}
