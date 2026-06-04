import numpy as np

L = 1.0
Nx = 120
dx = L / (Nx - 1)
x = np.linspace(0, L, Nx)

dt = 0.0005
Nt = 200

def run_sim(v, D):
    u = np.exp(-100 * (x - 0.3)**2)

    for n in range(Nt):
        u_new = u.copy()

        for i in range(1, Nx - 1):
            advection = -v * (u[i] - u[i - 1]) / dx
            diffusion = D * (u[i + 1] - 2*u[i] + u[i - 1]) / dx**2
            u_new[i] = u[i] + dt * (advection + diffusion)

        u = u_new

    return u


def plot_solution(x, u, filename="results/final_profile.txt"):
    import numpy as np
    np.savetxt(filename, u)
    print("Saved result profile to:", filename)