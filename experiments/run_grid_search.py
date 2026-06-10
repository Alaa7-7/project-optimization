import numpy as np
from src.diffusion import run_sim

def run_grid_search():

    true_v = 0.8
    true_D = 0.05

    v_values = np.linspace(0.5, 1.5, 10)
    D_values = np.linspace(0.01, 0.1, 10)

    u_target = run_sim(true_v, true_D)

    best_cost = float("inf")
    best_v = None
    best_D = None

    for v in v_values:
        for D in D_values:

            u = run_sim(v, D)
            cost = np.sum((u - u_target)**2)

            if cost < best_cost:
                best_cost = cost
                best_v = v
                best_D = D

    print("=== Grid Search Results ===")
    print("v =", best_v)
    print("D =", best_D)
    print("cost =", best_cost)