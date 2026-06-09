from fastapi import FastAPI
from src.solvers.genetic_solver import solve_genetic

app = FastAPI(title="Research Optimization System")

@app.post("/genetic-optimize")
def genetic_optimize(request: dict):
    n = request.get("size", 20)
    result = solve_genetic(n)

    return {
        "method": "genetic_algorithm",
        "result": result
    }

