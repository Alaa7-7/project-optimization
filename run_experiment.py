import numpy as np
from src.diffusion import run_sim

def run_full_pipeline():

    print("=== Bayesian-style Inverse Problem Optimization ===")

    true_v = 0.8
    true_D = 0.05

    u_target = run_sim(true_v, true_D)
    u_target = u_target + 0.01 * np.random.randn(len(u_target))

    samples_v = []
    samples_D = []
    costs = []

    N_iter = 200

    for i in range(N_iter):

        v = np.random.normal(0.8, 0.2)
        D = np.random.normal(0.05, 0.02)

        v = np.clip(v, 0.1, 2.0)
        D = np.clip(D, 0.001, 0.2)

        u = run_sim(v, D)

        cost = np.sum((u - u_target) ** 2)

        samples_v.append(v)
        samples_D.append(D)
        costs.append(cost)

    best_index = np.argmin(costs)

    best_v = samples_v[best_index]
    best_D = samples_D[best_index]

    print("\n=== Results ===")
    print("True v =", true_v, "| Estimated v =", best_v)
    print("True D =", true_D, "| Estimated D =", best_D)
    print("Min Error =", np.min(costs))

    u_best = run_sim(best_v, best_D)

    np.savetxt("results/final_solution.txt", u_best)

    print("Finished successfully.")