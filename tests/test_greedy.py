from src.problem import Problem
from src.greedy import greedy


def test_greedy():

    problem = Problem(n=4, budget=20)

    problem.cost = [10, 8, 5, 12]
    problem.value = [20, 24, 15, 18]

    solution = greedy(problem)

    cost, value = problem.evaluate(solution)

    assert cost <= problem.budget
    assert value > 0

    print("Solution:", solution)
    print("Cost:", cost)
    print("Value:", value)
    print("Greedy test passed")


if __name__ == "__main__":
    test_greedy()

