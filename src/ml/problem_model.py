import random

class OptimizationProblem:
    def __init__(self, n=20):
        self.n = n
        self.costs = [random.randint(1, 20) for _ in range(n)]
        self.values = [random.randint(5, 30) for _ in range(n)]

    def fitness(self, solution):
        cost = sum(self.costs[i] for i in solution)
        value = sum(self.values[i] for i in solution)

        efficiency = value / (cost + 1)

        return {
            "cost": cost,
            "value": value,
            "efficiency": efficiency
        }
