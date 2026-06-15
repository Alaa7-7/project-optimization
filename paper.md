#  Inverse Modeling and Optimization of the Advection–Diffusion Equation

##  Abstract

This project presents a method for solving inverse problems based on the one-dimensional Advection–Diffusion equation. The goal is to estimate unknown physical parameters (advection velocity and diffusion coefficient) using numerical simulation combined with optimization algorithms. The method combines a finite difference solver with heuristic optimization methods such as Genetic Algorithms (GA). The results demonstrate accurate recovery of the unknown parameters with low estimation error, showing the effectiveness of combining numerical PDE solvers with optimization techniques.

---

## 1. Introduction

Inverse problems in partial differential equations (PDEs) are fundamental in scientific computing, where unknown physical parameters must be estimated from observed data. This work focuses on estimating the velocity and diffusion in a transport system modeled by the Advection–Diffusion equation. This work was developed as part of an optimization course project.

The project combines:
- Numerical PDE simulation
- Synthetic data generation
- Optimization-based parameter estimation

---

## 2. Mathematical Model

The system is governed by the 1D Advection–Diffusion equation:

\[
\frac{\partial u}{\partial t} + v \frac{\partial u}{\partial x}
= D \frac{\partial^2 u}{\partial x^2}
\]

Where:
- \( u(x,t) \): transported scalar field
- \( v \): advection velocity (unknown)
- \( D \): diffusion coefficient (unknown)

---

## 3. Numerical Method (Forward Solver)

The PDE is solved using the Finite Difference Method (FDM):

### Advection term:
\[
\frac{\partial u}{\partial x} \approx \frac{u_i - u_{i-1}}{\Delta x}
\]

### Diffusion term:
\[
\frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2}
\]

The time integration is performed using an explicit Euler scheme:

\[
u^{n+1} = u^n + \Delta t \cdot (\text{advection} + \text{diffusion})
\]

---

## 4. Inverse Problem Formulation

The objective is to estimate \( v \) and \( D \) by minimizing the following loss function:

\[
J(v, D) = \| u_{sim}(v, D) - u_{obs} \|_2^2
\]

Where:
- \( u_{sim} \): numerical solution from PDE solver
- \( u_{obs} \): observed (synthetic) data

---

## 5. Optimization Methods

The following optimization techniques are used:

### 5.1 Genetic Algorithm (GA)
- Population-based search
- Selection and crossover
- Global exploration of parameter space


---

## 6. Experimental Setup

- True parameters:
  - \( v = 0.8 \)
  - \( D = 0.05 \)

- Spatial grid: 1D domain discretization
- Time stepping: explicit finite difference scheme
- Multiple runs to evaluate stability

---

## 7. Results

### 7.1 Estimated Parameters

| Method | v estimate | D estimate |
|--------|------------|------------|
| GA     | ~0.78      | ~0.0508    |

---

### 7.2 Error Analysis

- GA shows very low error:
  - \( v \) error ˜ 0.0075
  - \( D \) error ˜ 0.00026

- GA shows stable convergence and low estimation error across runs.
- Results correspond to a single stochastic run of the optimization algorithm and may vary across different executions.

---

### 7.3 Statistical Behavior


- The Genetic Algorithm exhibits stochastic behavior due to its population-based search strategy, which may lead to variations across different runs.

---

## 8. Discussion

The results demonstrate that optimization algorithms can successfully solve inverse PDE problems when combined with numerical solvers. The results demonstrate that the Genetic Algorithm (GA) is effective in solving the inverse problem for the Advection–Diffusion equation, achieving accurate parameter estimation with stable convergence. The algorithm provides a balance between exploration and convergence, leading to reliable optimization performance.

The small estimation error confirms that the model is capable of recovering unknown physical parameters from synthetic observations.

---

## 9. Conclusion

This study presents a modular computational framework for inverse parameter estimation in PDE systems. The combination of finite difference simulation and heuristic optimization proves effective for recovering unknown parameters with high accuracy.

The approach can be extended to more complex physical systems and higher-dimensional PDEs.

---

## 10. Future Work

- Extension to 2D and 3D PDE systems
- Incorporation of noise in observations
- Bayesian optimization methods
- Neural network-based surrogate modeling
- Real experimental data validation

---

##  Applications

- Fluid dynamics
- Heat transfer systems
- Inverse problems in physics
- Scientific machine learning
- Engineering parameter estimation

---

## Summary

This project demonstrates that inverse problems in PDEs can be effectively solved using computational optimization techniques, this project show how optimization methods can be used to estimate unknown parameters on PDE models.