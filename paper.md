 Numerical Study of the 1D Advection–Diffusion Equation with Parameter Optimization

 Abstract
This work presents a numerical solution of the one-dimensional Advection–Diffusion equation using the Finite Difference Method. A simple optimization approach is applied to estimate the physical parameters of the system.

---

 1. Introduction
The Advection–Diffusion equation describes transport phenomena in physics and engineering. It combines transport (advection) and spreading (diffusion) effects.

---

 2. Governing Equation

du/dt + v du/dx = D d²u/dx²

Where:
- u(x,t): transported quantity  
- v: velocity  
- D: diffusion coefficient  

---

 3. Numerical Method
The equation is solved using:
- Finite Difference Method (FDM)
- Explicit time stepping scheme
- Discretization in space and time

---

4. Optimization Strategy
The parameters (v, D) are selected using a grid search method that minimizes a cost function defined as:

J = S u(x,T)²

---

 5. Results
The model returns:
- Optimal velocity (v)
- Optimal diffusion coefficient (D)
- Final concentration profile

The results show stable numerical behavior and physically consistent diffusion patterns.

---

 6. Conclusion
A simple but effective numerical framework was developed to solve and optimize the Advection–Diffusion system. The method can be extended to more complex inverse problems and real-world applications.