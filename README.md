 Advection–Diffusion Optimization Project

 Overview
This project implements a numerical solution of the 1D Advection–Diffusion equation and performs parameter optimization to identify the best physical parameters (velocity and diffusion coefficient).

---

 Governing Equation

The system is governed by the Advection–Diffusion equation:

?u/?t + v ?u/?x = D ?²u/?x²

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

- src/ ? numerical solver
- main.py ? optimization pipeline
- results/ ? simulation outputs
- figures/ ? future plots

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