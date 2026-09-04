from src.problem import Problem


def test_evaluate():

    problem = Problem(n=3, budget=20)

    problem.cost = [10, 15, 5]
    problem.value = [20, 30, 10]

    solution = [1, 0, 1]

    cost, value = problem.evaluate(solution)

    assert cost == 15
    assert value == 30


if __name__ == "__main__":
    test_evaluate()
    print("Test passed")
