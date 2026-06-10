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