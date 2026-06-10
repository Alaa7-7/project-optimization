import numpy as np

def analyze_results():

    print("=== Scientific Results Analysis (No Plots Version) ===")

    # ------------------------
    # Load data
    # ------------------------
    v = np.loadtxt("results/samples_v.txt")
    D = np.loadtxt("results/samples_D.txt")
    cost = np.loadtxt("results/costs.txt")

    # ------------------------
    # Safety checks
    # ------------------------
    if len(v) == 0 or len(D) == 0 or len(cost) == 0:
        print("Error: Empty dataset!")
        return

    # ------------------------
    # Parameter v statistics
    # ------------------------
    v_mean = np.mean(v)
    v_std = np.std(v)
    v_min = np.min(v)
    v_max = np.max(v)

    # ------------------------
    # Parameter D statistics
    # ------------------------
    D_mean = np.mean(D)
    D_std = np.std(D)
    D_min = np.min(D)
    D_max = np.max(D)

    # ------------------------
    # Cost cleaning (robust statistics)
    # ------------------------
    cost = np.array(cost)

    # remove invalid values
    cost = cost[np.isfinite(cost)]

    # remove extreme outliers (95% filter)
    p95 = np.percentile(cost, 95)
    cost = cost[cost < p95]
    cost = cost[cost > 0]

    # ------------------------
    # Cost statistics
    # ------------------------
    cost_min = np.min(cost)
    cost_max = np.max(cost)
    cost_mean = np.mean(cost)
    cost_std = np.std(cost)

    # ------------------------
    # Extra scientific metric (VERY IMPORTANT)
    # ------------------------
    relative_improvement = (cost_max - cost_min) / (cost_max + 1e-8)

    # ------------------------
    # Print report
    # ------------------------
    print("\n--- Parameter v ---")
    print("Mean:", v_mean)
    print("Std :", v_std)
    print("Min :", v_min)
    print("Max :", v_max)

    print("\n--- Parameter D ---")
    print("Mean:", D_mean)
    print("Std :", D_std)
    print("Min :", D_min)
    print("Max :", D_max)

    print("\n--- Cost Function ---")
    print("Min cost :", cost_min)
    print("Max cost :", cost_max)
    print("Mean cost:", cost_mean)
    print("Std cost :", cost_std)

    print("\n--- Performance Metric ---")
    print("Relative improvement:", relative_improvement)

    # ------------------------
    # Save report
    # ------------------------
    with open("results/scientific_report.txt", "w") as f:
        f.write("=== Scientific Report ===\n\n")

        f.write("Parameter v:\n")
        f.write(f"Mean = {v_mean}\n")
        f.write(f"Std  = {v_std}\n")
        f.write(f"Min  = {v_min}\n")
        f.write(f"Max  = {v_max}\n\n")

        f.write("Parameter D:\n")
        f.write(f"Mean = {D_mean}\n")
        f.write(f"Std  = {D_std}\n")
        f.write(f"Min  = {D_min}\n")
        f.write(f"Max  = {D_max}\n\n")

        f.write("Cost Function:\n")
        f.write(f"Min cost  = {cost_min}\n")
        f.write(f"Max cost  = {cost_max}\n")
        f.write(f"Mean cost = {cost_mean}\n")
        f.write(f"Std cost  = {cost_std}\n\n")

        f.write("Performance Metric:\n")
        f.write(f"Relative improvement = {relative_improvement}\n")

    print("\nReport saved to results/scientific_report.txt")


if __name__ == "__main__":
    analyze_results()