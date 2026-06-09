class OptimizationProblem:
    def __init__(self, data):
        self.data = data

    def objective(self):
        return "minimize cost"

    def constraints(self):
        return "resource limits"