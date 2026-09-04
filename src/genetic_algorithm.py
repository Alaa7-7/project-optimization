
import random


def genetic_algorithm(problem, population_size=10, generations=30):

    population = []

    for _ in range(population_size):

        solution = []

        for i in range(problem.n):
            solution.append(random.randint(0, 1))

        cost, value = problem.evaluate(solution)

        while cost > problem.budget:
            selected = []

            for i in range(problem.n):
                if solution[i] == 1:
                    selected.append(i)

            i = random.choice(selected)
            solution[i] = 0

            cost, value = problem.evaluate(solution)

        population.append(solution)

    best_solution = population[0][:]
    best_cost, best_value = problem.evaluate(best_solution)

    for _ in range(generations):

        good_solutions = []

        for solution in population:

            cost, value = problem.evaluate(solution)

            if cost <= problem.budget:
                good_solutions.append(solution)

                if value > best_value:
                    best_solution = solution[:]
                    best_value = value

        good_solutions.sort(
            key=lambda solution: problem.evaluate(solution)[1],
            reverse=True
        )

        new_population = good_solutions[:2]

        while len(new_population) < population_size:

            p1, p2 = random.sample(good_solutions, 2)

            point = random.randint(1, problem.n - 1)

            child = p1[:point] + p2[point:]

            if random.random() < 0.1:

                i = random.randint(0, problem.n - 1)

                if child[i] == 0:
                    child[i] = 1
                else:
                    child[i] = 0

            cost, value = problem.evaluate(child)

            if cost <= problem.budget:
                new_population.append(child)

        population = new_population

    return best_solution
