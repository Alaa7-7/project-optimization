import random
from src.ml.problem_model import OptimizationProblem
from src.solvers.genetic_solver import solve_genetic

#  Greedy Algorithm
def greedy_solver(n=20):
    problem = OptimizationProblem(n)

    selected = list(range(n//2))

    return problem.fitness(selected)

#  Random Algorithm
def random_solver(n=20):
    problem = OptimizationProblem(n)

    selected = random.sample(range(n), k=n//2)

    return problem.fitness(selected)

#  Genetic Algorithm
def genetic_solver(n=20):
    return solve_genetic(n)

#  Run all comparisons
def run_comparison(n=20):
    greedy = greedy_solver(n)
    random = random_solver(n)
    genetic = genetic_solver(n)

    return {
        "greedy": greedy,
        "random": random,
        "genetic": genetic
    }
