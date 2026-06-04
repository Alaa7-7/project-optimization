import numpy as np
from src.diffusion import run_sim, plot_solution

# run best simulation (from optimization result)
v = 1.0
D = 0.02

L = 1.0
Nx = 120
x = np.linspace(0, L, Nx)

u = run_sim(v, D)

# save data
np.savetxt("results/final_result.txt", u)

# plot result
plot_solution(x, u)

print("Simulation + visualization completed")