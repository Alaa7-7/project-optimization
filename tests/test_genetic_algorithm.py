from src.problem import Problem
from src.genetic_algorithm import genetic_algorithm


def test_genetic_algorithm():

    problem = Problem(n=4, budget=20)

    problem.cost = [10, 8, 5, 12]
    problem.value = [20, 24, 15, 18]

    solution = genetic_algorithm(
        problem,
        population_size=10,
        generations=30
    )

    cost, value = problem.evaluate(solution)

    assert cost <= problem.budget
    assert value > 0

    print("Solution:", solution)
    print("Cost:", cost)
    print("Value:", value)
    print("Genetic Algorithm test passed")


if __name__ == "__main__":
    test_genetic_algorithm()