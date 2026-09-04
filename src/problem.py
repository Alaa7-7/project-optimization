import random


class Problem:
    def __init__(self, n=10, budget=50):
        self.n = n
        self.budget = budget

        self.cost = [random.randint(5, 20) for _ in range(n)]
        self.value = [random.randint(10, 40) for _ in range(n)]

    def evaluate(self, solution):
        total_cost = 0
        total_value = 0

        for i in range(self.n):
            if solution[i] == 1:
                total_cost += self.cost[i]
                total_value += self.value[i]

        return total_cost, total_value