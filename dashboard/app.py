import streamlit as st
from src.solvers.exact_solver import solve_exact

st.title(" AI Optimization Dashboard")

st.write("Interactive AI Optimization System")

size = st.slider("Problem Size", 5, 100, 20)

if st.button("Run Optimization"):
    result = solve_exact({"size": size})

    st.subheader(" Results")

    st.json(result)

    st.metric("Cost", result["cost"])
    st.metric("Efficiency", result["efficiency_score"])
