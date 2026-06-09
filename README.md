 Advection–Diffusion Optimization Project

 Overview
This project implements a numerical solution of the 1D Advection–Diffusion equation and performs parameter optimization to identify the best physical parameters (velocity and diffusion coefficient).It also generates a final analysis report saved in the results/ folder.

---

 Governing Equation

The system is governed by the Advection–Diffusion equation:

du/dt + v du/dx = D d²u/dx²

Where:
- u(x,t): transported quantity
- v: advection velocity
- D: diffusion coefficient

---

 Objective

The goal is to find optimal values of:
- v (velocity)
- D (diffusion coefficient)

that minimize the following cost function:

J = S u(x,T)²

---

 Methodology

- Finite Difference Method (FDM)
- Explicit time stepping scheme
- Grid search optimization
- Parameter sweep over (v, D)

---

 Project Structure

- src/  numerical solver
- main.py  optimization pipeline
- results/  simulation outputs
- figures/  future plots

---

 Output

The program returns:
- Best v
- Best D
- Minimum cost value
- Final numerical solution

---

 How to Run

bash
python main.py


---

 Features
- Diffusion-based simulation model
- Dynamic visualization and animation
- Automatic result export
- Scientific-style documentation (paper included)

---

 Project Structure
---

How to Run

-- bash id="run1"
python main.py