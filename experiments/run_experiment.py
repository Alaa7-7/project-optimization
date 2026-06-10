def run_full_pipeline():

    print("=== Bayesian Inverse Problem with Uncertainty ===")

    import numpy as np
    from src.diffusion import run_sim

    true_v = 0.8
    true_D = 0.05

    u_target = run_sim(true_v, true_D)
    u_target = u_target + 0.01 * np.random.randn(len(u_target))

    samples_v = []
    samples_D = []
    costs = []

    N_iter = 400

    for i in range(N_iter):

        # sampling (bounded stochastic search)
        v = np.clip(np.random.normal(0.8, 0.12), 0.4, 1.2)
        D = np.clip(np.random.normal(0.05, 0.01), 0.01, 0.1)

        # extra safety bounds
        v = np.clip(v, 0.1, 2.0)
        D = np.clip(D, 0.001, 0.2)

        # forward model
        u = run_sim(v, D)

        # numerical safety
        u = np.nan_to_num(u, nan=0.0, posinf=1e3, neginf=-1e3)

        # skip unstable solutions (IMPORTANT)
        if np.max(np.abs(u)) > 1e3:
            continue

        # cost function (normalized L2)
        cost = np.linalg.norm(u - u_target) / (np.linalg.norm(u_target) + 1e-8)

        samples_v.append(v)
        samples_D.append(D)
        costs.append(cost)

    # safety check (avoid crash if all skipped)
    if len(costs) == 0:
        print("No valid samples found!")
        return

    best_idx = np.argmin(costs)

    best_v = samples_v[best_idx]
    best_D = samples_D[best_idx]

    print("\n=== Results ===")
    print("True v =", true_v)
    print("Estimated v =", best_v)
    print("True D =", true_D)
    print("Estimated D =", best_D)
    print("Min cost =", np.min(costs))

    # final best simulation
    u_best = run_sim(best_v, best_D)
    u_best = np.nan_to_num(u_best, nan=0.0, posinf=1e3, neginf=-1e3)

    # save results
    np.savetxt("results/final_solution.txt", u_best)
    np.savetxt("results/samples_v.txt", samples_v)
    np.savetxt("results/samples_D.txt", samples_D)
    np.savetxt("results/costs.txt", costs)

    print("Finished successfully.")