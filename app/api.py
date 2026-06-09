from fastapi import FastAPI
from src.solvers.exact_solver import solve_exact

app = FastAPI(title="AI Optimization Engine")

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "AI Optimization Engine is active"
    }

@app.post("/optimize")
def optimize(request: dict):
    result = solve_exact(request)

    return {
        "status": "success",
        "input": request,
        "result": result
    }
