from src.solvers.comparison import run_comparison


def benchmark(n=20, runs=20):

    greedy_eff = 0
    random_eff = 0
    genetic_eff = 0

    greedy_time = 0
    random_time = 0
    genetic_time = 0

    for _ in range(runs):

        result = run_comparison(n)

        greedy_eff += result["greedy"]["efficiency"]
        random_eff += result["random"]["efficiency"]
        genetic_eff += result["genetic"]["efficiency"]

        greedy_time += result["greedy"]["time"]
        random_time += result["random"]["time"]
        genetic_time += result["genetic"]["time"]

    return {
        "greedy": {
            "avg_efficiency": round(greedy_eff / runs, 3),
            "avg_time": round(greedy_time / runs, 6)
        },

        "random": {
            "avg_efficiency": round(random_eff / runs, 3),
            "avg_time": round(random_time / runs, 6)
        },

        "genetic": {
            "avg_efficiency": round(genetic_eff / runs, 3),
            "avg_time": round(genetic_time / runs, 6)
        }
    }