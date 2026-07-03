from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router

# Initialize app
app = FastAPI(
    title="School ERP API",
    description="An API for  School ERP application",
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

app.include_router(api_router, prefix="/api/v1")


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Hayatul SIMS API"}
