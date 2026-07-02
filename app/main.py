from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize app
app = FastAPI(
    title="Hayatul SIMS API",
    description="An API for  Hayatul SIMS application",
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


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Hayatul SIMS API"}
