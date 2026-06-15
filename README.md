#  Scientific Optimization & Inverse Modeling

##  Overview

This repository contains a computational project for:

1. Scientific numerical simulation of partial differential equations (PDEs)
2. Optimization-based parameter estimation (inverse problems)
3. Benchmarking of heuristic optimization algorithms

The project combines:
- Numerical PDE solver (Advection–Diffusion equation)
- Inverse problem solving
- Optimization algorithms (GA / Random Search)

This project was developed as part of an optimization course. The goal is to estimate unknown parameters in an advection-diffusion equation and compare the performance of GA (Genetic Algorithm).

---

#  Mathematical Model

##  Advection–Diffusion Equation

The system is based on the following PDE:

\[
\frac{\partial u}{\partial t} + v \frac{\partial u}{\partial x}
= D \frac{\partial^2 u}{\partial x^2}
\]

Where:

- \( u(x,t) \): concentration or transported quantity
- \( v \): advection velocity (unknown parameter)
- \( D \): diffusion coefficient (unknown parameter)

---

##  Inverse Problem Objective

We aim to estimate unknown parameters \( v \) and \( D \) from observed data:

\[
\min_{v, D} \; \| u_{sim}(v, D) - u_{obs} \|_2^2
\]

where:

- \( u_sim \) : simulated solution from the PDE model
- \( u_obs \) : observed data

The objective is to find the values of v and D by minimizing the difference between simulated and observed data.

---

#  Methodology

## 1. Forward Solver (PDE Simulation)

- Finite Difference Method (FDM)
- Explicit time stepping
- Upwind scheme for advection
- Central difference for diffusion

Used to generate synthetic observed data.

---

## 2. Inverse Solver

We estimate parameters using optimization algorithms:

###  Genetic Algorithm (GA)
- Population-based search
- Selection and crossover
- Global exploration


---

#  Optimization Process

1. Initialize candidate solutions (v, D)
2. Simulate PDE using forward solver
3. Compute loss between simulation and observed data
4. Evaluate the objective function
5. Select the best parameter estimates

Note: Results may vary across runs due to stochastic optimization.

---

#  Results

##  True Parameters

- \( v = 0.8 \)
- \( D = 0.05 \)

---

##  Estimated Results

| Method | v estimate | D estimate | 
|--------|------------|------------|
| GA     | ~0.7945     | ~0.05077    | 

---

##  Error Analysis

- GA:
  - v error = 0.0055
  - D error = 0.00077

Results represent a single stochastic run of the algorithm.

---

#  Project Structure
project-optimization/
¦
+-- src/
¦   +-- diffusion.py
¦   +-- solvers/
¦   ¦   +-- genetic_solver.py
¦   ¦   +-- exact_solver.py
¦   ¦   +-- benchmark.py
¦   ¦   +-- comparison.py
¦   +-- ml/
¦   +-- core/
¦
+-- experiments/
¦   +-- run_experiment.py
¦
+-- results/
+-- figures/
+-- paper.tex
+-- README.md

---

#  How to Run

## 1. Setup environment

```bash
python -m venv venv
venv\Scripts\activate
python main.py


##  Output

After running the experiments, the system produces:

- Estimated parameters for each optimization method
- Cost / fitness values
- Error statistics (mean and standard deviation)
- Saved result files inside the results/ folder

Example output:
- True v = 0.8, True D = 0.05
- Estimated v ˜ 0.80
- Estimated D ˜ 0.05

---

##  Summary

This project demonstrates a method for solving inverse problems using numerical simulation and optimization algorithms.

Key points:

- The system solves a simplified PDE-based model
- Unknown parameters are estimated using optimization methods
- Genetic Algorithm (GA) 


---

## Keys

Combining numerical PDE simulation with heuristic optimization is an effective approach for parameter estimation in synthetic scientific systems.
