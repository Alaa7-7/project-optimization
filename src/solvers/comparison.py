import random
import time

from src.ml.problem_model import OptimizationProblem
from src.solvers.genetic_solver import solve_genetic


# Greedy Algorithm
def greedy_solver(n=20):
    problem = OptimizationProblem(n)

    selected = list(range(n // 2))

    return problem.fitness(selected)


# Random Algorithm
def random_solver(n=20):
    problem = OptimizationProblem(n)

    selected = random.sample(range(n), k=n // 2)

    return problem.fitness(selected)


# Genetic Algorithm
def genetic_solver(n=20):
    return solve_genetic(n)


# Run all comparisons
def run_comparison(n=20):

    start = time.perf_counter()
    greedy = greedy_solver(n)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    random_result = random_solver(n)
    random_time = time.perf_counter() - start

    start = time.perf_counter()
    genetic = genetic_solver(n)
    genetic_time = time.perf_counter() - start

    greedy["time"] = round(greedy_time, 6)
    random_result["time"] = round(random_time, 6)
    genetic["time"] = round(genetic_time, 6)

    return {
        "greedy": greedy,
        "random": random_result,
        "genetic": genetic
    }
