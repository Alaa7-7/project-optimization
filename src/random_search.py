import random


def random_search(problem, runs=100):

    best_solution = None
    best_value = 0

    for _ in range(runs):

        solution = []

        for i in range(problem.n):
            solution.append(random.randint(0, 1))

        cost, value = problem.evaluate(solution)

        if cost <= problem.budget and value > best_value:
            best_solution = solution
            best_value = value

    return best_solution