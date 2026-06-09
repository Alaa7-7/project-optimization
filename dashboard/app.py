import streamlit as st
from src.solvers.genetic_solver import solve_genetic

st.title("Research-Grade Optimization System")

n = st.slider("Problem Size", 10, 100, 20)

if st.button("Run Genetic Algorithm"):
    result = solve_genetic(n)

    st.subheader("Best Solution")
    st.json(result)

    st.metric("Cost", result["cost"])
    st.metric("Efficiency", result["efficiency"])
