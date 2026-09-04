import time

from src.problem import Problem
from src.greedy import greedy
from src.random_search import random_search
from src.genetic_algorithm import genetic_algorithm


def multiple_runs(runs=10):

    greedy_value = 0
    greedy_cost = 0
    greedy_time = 0

    random_value = 0
    random_cost = 0
    random_time = 0

    genetic_value = 0
    genetic_cost = 0
    genetic_time = 0

    for _ in range(runs):

        problem = Problem()

        start = time.perf_counter()
        greedy_solution = greedy(problem)
        greedy_time += time.perf_counter() - start

        start = time.perf_counter()
        random_solution = random_search(problem)
        random_time += time.perf_counter() - start

        start = time.perf_counter()
        genetic_solution = genetic_algorithm(problem)
        genetic_time += time.perf_counter() - start

        cost, value = problem.evaluate(greedy_solution)
        greedy_cost += cost
        greedy_value += value

        cost, value = problem.evaluate(random_solution)
        random_cost += cost
        random_value += value

        cost, value = problem.evaluate(genetic_solution)
        genetic_cost += cost
        genetic_value += value

    print("=== Multiple Runs Results ===")
    print("Runs:", runs)
    print()

    print("Greedy")
    print("Average Cost:", round(greedy_cost / runs, 2))
    print("Average Value:", round(greedy_value / runs, 2))
    print("Average Time:", round(greedy_time / runs, 6))
    print()

    print("Random Search")
    print("Average Cost:", round(random_cost / runs, 2))
    print("Average Value:", round(random_value / runs, 2))
    print("Average Time:", round(random_time / runs, 6))
    print()

    print("Genetic Algorithm")
    print("Average Cost:", round(genetic_cost / runs, 2))
    print("Average Value:", round(genetic_value / runs, 2))
    print("Average Time:", round(genetic_time / runs, 6))


if __name__ == "__main__":
    multiple_runs()
