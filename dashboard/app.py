import streamlit as st
from src.solvers.comparison import run_comparison

st.title(" AI Optimization Research Dashboard")

n = st.slider("Problem Size", 10, 100, 20)

if st.button("Run Comparison"):
    result = run_comparison(n)

    st.json(result)

    labels = ["Greedy", "Random", "Genetic"]

    efficiency = [
        result["greedy"]["efficiency"],
        result["random"]["efficiency"],
        result["genetic"]["efficiency"]
    ]

    cost = [
        result["greedy"]["cost"],
        result["random"]["cost"],
        result["genetic"]["cost"]
    ]

    st.subheader(" Efficiency")
    st.bar_chart(dict(zip(labels, efficiency)))

    st.subheader(" Cost")
    st.bar_chart(dict(zip(labels, cost)))