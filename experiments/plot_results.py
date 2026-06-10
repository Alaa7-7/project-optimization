import numpy as np
import matplotlib.pyplot as plt

# load results
v = np.loadtxt("results/samples_v.txt")
D = np.loadtxt("results/samples_D.txt")
cost = np.loadtxt("results/costs.txt")

# -------------------
# v distribution
# -------------------
plt.figure()
plt.hist(v, bins=30)
plt.title("Distribution of v (Bayesian Sampling)")
plt.xlabel("v")
plt.ylabel("Frequency")
plt.show()

# -------------------
# D distribution
# -------------------
plt.figure()
plt.hist(D, bins=30)
plt.title("Distribution of D (Bayesian Sampling)")
plt.xlabel("D")
plt.ylabel("Frequency")
plt.show()

# -------------------
# cost convergence
# -------------------
plt.figure()
plt.plot(cost)
plt.title("Cost Evolution")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()
