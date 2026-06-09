import random
from src.ml.problem_model import OptimizationProblem

def solve_genetic(n=20, generations=50):
    problem = OptimizationProblem(n)

    population = [
        random.sample(range(n), k=random.randint(3, n//2))
        for _ in range(10)
    ]

    def fitness(sol):
        return problem.fitness(sol)["efficiency"]

    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)

        parents = population[:5]

        children = []
        for _ in range(5):
            p1, p2 = random.sample(parents, 2)
            child = list(set(p1[:len(p1)//2] + p2[len(p2)//2:]))
            children.append(child)

        population = parents + children

    best = max(population, key=fitness)

    result = problem.fitness(best)

    return {
        "solution": best,
        "cost": result["cost"],
        "value": result["value"],
        "efficiency": result["efficiency"]
    }