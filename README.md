  Scientific Computing and AI Optimization Projects

This repository contains two research-level projects in scientific computing and optimization.

---

 ?Advection–Diffusion Optimization Project

 Overview
This project implements a numerical solution of the 1D Advection–Diffusion equation and performs parameter optimization to identify the best physical parameters (velocity and diffusion coefficient).

---

 Governing Equation

du/dt + v du/dx = D d²u/dx²

Where:
- u(x,t): transported quantity  
- v: advection velocity  
- D: diffusion coefficient  

---

 Objective

Minimize:

J = ? u(x,T)² dx

by finding optimal:
- v (velocity)
- D (diffusion coefficient)

---

 Methodology

- Finite Difference Method (FDM)
- Explicit time stepping scheme
- Grid search optimization
- Parameter sweep over (v, D)

---

 Output

- Optimal v
- Optimal D
- Minimum cost value
- Final numerical solution

---

 How to Run

bash
python main.py



Outputs


 Comparative Study

This project compares two inverse problem approaches:

 1. Grid Search (Classical Method)
- Deterministic parameter sweep
- Low computational efficiency
- Baseline method

 2. Bayesian Sampling (Proposed Method)
- Stochastic inference approach
- Provides uncertainty estimation
- More efficient exploration of parameter space



 Scientific Contribution

The key contribution of this work is the comparison between:

- Traditional optimization methods
- Probabilistic Bayesian inference

for solving inverse PDE problems.

 Results

The proposed Bayesian-inspired inverse method was evaluated on a synthetic advection–diffusion system with known ground-truth parameters.

 True vs Estimated Parameters

| Parameter | True Value | Estimated Value |
|----------|------------|----------------|
| v (velocity) | 0.8 | 0.7939 |
| D (diffusion) | 0.05 | 0.0497 |

The model successfully recovered the unknown parameters with high accuracy, achieving less than 2% relative error.



 Cost Function Analysis

- Minimum cost achieved: *0.0415*
- Mean cost: *0.0842*
- Standard deviation: *0.0293*
- Maximum cost: *0.1546*

These values indicate stable convergence of the optimization process without numerical divergence.



 Statistical Behavior of Sampling

- v mean: 0.8075 (close to true value 0.0
- v std: 0.1171 (controlled exploration)
- D mean: 0.0490 (very close to true value 0.05)
- D std: 0.0093 (high stability)

---

 Optimization Quality Metric

Relative improvement score:

\[
\text{RI} = 0.7312
\]

This indicates strong convergence behavior and effective exploration of the parameter space.


 Key Insight

The Bayesian-inspired stochastic optimization method provides:
- Accurate parameter recovery
- Stable convergence under noise
- Robust performance for inverse PDE problems

 Interpretation of Results

The results show that the proposed method is able to correctly identify the unknown physical parameters of the advection–diffusion system.

Even under noisy observations, the algorithm maintains stable convergence and avoids numerical instability.

The close agreement between true and estimated values confirms the effectiveness of combining:
- Numerical PDE simulation
- Stochastic Bayesian-inspired optimization
- L2-based cost minimization

This demonstrates that the method is suitable for solving inverse problems in computational physics.
