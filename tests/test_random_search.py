from src.problem import Problem
from src.random_search import random_search


def test_random_search():

    problem = Problem(n=4, budget=20)

    problem.cost = [10, 8, 5, 12]
    problem.value = [20, 24, 15, 18]

    solution = random_search(problem, runs=100)

    cost, value = problem.evaluate(solution)

    assert cost <= problem.budget
    assert value > 0

    print("Solution:", solution)
    print("Cost:", cost)
    print("Value:", value)
    print("Random Search test passed")


if __name__ == "__main__":
    test_random_search()