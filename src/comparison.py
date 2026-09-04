import time

from src.problem import Problem
from src.greedy import greedy
from src.random_search import random_search
from src.genetic_algorithm import genetic_algorithm


def run_comparison():

    problem = Problem()

    start = time.perf_counter()
    greedy_solution = greedy(problem)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    random_solution = random_search(problem)
    random_time = time.perf_counter() - start

    start = time.perf_counter()
    genetic_solution = genetic_algorithm(problem)
    genetic_time = time.perf_counter() - start

    greedy_cost, greedy_value = problem.evaluate(greedy_solution)
    random_cost, random_value = problem.evaluate(random_solution)
    genetic_cost, genetic_value = problem.evaluate(genetic_solution)

    print("=== Optimization Comparison ===")
    print("Budget:", problem.budget)
    print()

    print("Greedy")
    print("Cost:", greedy_cost)
    print("Value:", greedy_value)
    print("Time:", round(greedy_time, 6))
    print()

    print("Random Search")
    print("Cost:", random_cost)
    print("Value:", random_value)
    print("Time:", round(random_time, 6))
    print()

    print("Genetic Algorithm")
    print("Cost:", genetic_cost)
    print("Value:", genetic_value)
    print("Time:", round(genetic_time, 6))


if __name__ == "__main__":
    run_comparison()
