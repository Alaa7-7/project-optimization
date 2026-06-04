import numpy as np

# domain
L = 1.0
Nx = 120
dx = L / (Nx - 1)
x = np.linspace(0, L, Nx)

# time
dt = 0.0005
Nt = 300

# parameters
D = 0.01
v = 0.6

# initial condition
u = np.exp(-100 * (x - 0.3)**2)

# simulation
for n in range(Nt):
    u_new = u.copy()

    for i in range(1, Nx-1):
        advection = -v * (u[i] - u[i-1]) / dx
        diffusion = D * (u[i+1] - 2*u[i] + u[i-1]) / dx**2
        u_new[i] = u[i] + dt * (advection + diffusion)

    u = u_new

# save results to file instead of plotting
np.savetxt("result.txt", np.column_stack((x, u)))

print("Done: result.txt created")