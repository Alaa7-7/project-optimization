from src.problem import Problem


def greedy(problem):

    ratio = []

    for i in range(problem.n):
        r = problem.value[i] / problem.cost[i]
        ratio.append((r, i))

    ratio.sort(reverse=True)

    solution = [0] * problem.n
    total_cost = 0

    for r, i in ratio:
        if total_cost + problem.cost[i] <= problem.budget:
            solution[i] = 1
            total_cost += problem.cost[i]

    return solution