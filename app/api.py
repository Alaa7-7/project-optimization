from fastapi import FastAPI
from src.solvers.exact_solver import solve_exact

app = FastAPI(title="Optimization Engine API")

@app.get("/")
def home():
    return {"message": "Optimization API is running"}

@app.post("/optimize")
def optimize(request: dict):
    result = solve_exact(request)
    return {
        "status": "success",
        "solution": result
    }
