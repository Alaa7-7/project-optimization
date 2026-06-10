import numpy as np
from src.diffusion import run_sim

def run_full_pipeline():

    print("=== Inverse Problem Optimization Started ===")

    true_v = 0.8
    true_D = 0.05

    u_target = run_sim(true_v, true_D)
    u_target = u_target + 0.01 * np.random.randn(len(u_target))

    v_values = np.linspace(0.5, 1.5, 10)
    D_values = np.linspace(0.01, 0.1, 10)

    best_cost = float("inf")
    best_v = None
    best_D = None

    for v in v_values:
        for D in D_values:

            u = run_sim(v, D)

            cost = np.sum((u - u_target) ** 2)

            if cost < best_cost:
                best_cost = cost
                best_v = v
                best_D = D

    print("\n=== Inverse Problem Results ===")
    print("True v =", true_v, "| Estimated v =", best_v)
    print("True D =", true_D, "| Estimated D =", best_D)
    print("Error =", best_cost)

    u_best = run_sim(best_v, best_D)

    np.savetxt("results/final_solution.txt", u_best)

    print("Experiment completed successfully.")