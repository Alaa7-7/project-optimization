import streamlit as st
from src.solvers.exact_solver import solve_exact

st.title("AI Optimization Dashboard")

size = st.slider("Problem Size", 5, 100, 20)

if st.button("Run Optimization"):
    result = solve_exact({"size": size})

    st.json(result)

    st.metric("Cost", result["cost"])
    st.metric("Efficiency", result["efficiency_score"])