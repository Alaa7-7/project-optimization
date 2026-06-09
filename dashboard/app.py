import streamlit as st
from src.solvers.comparison import run_comparison

st.title(" AI Optimization Research Dashboard")

st.write("Compare Greedy, Random and Genetic algorithms")

n = st.slider("Problem Size", 10, 100, 20)

if st.button("Run Comparison"):

    result = run_comparison(n)

    st.subheader(" Results")

    st.markdown("### Greedy Algorithm")
    st.text(
        f"Efficiency: {result['greedy']['efficiency']:.3f}"
    )
    st.text(
        f"Execution Time: {result['greedy']['time']} sec"
    )

    st.markdown("### Random Algorithm")
    st.text(
        f"Efficiency: {result['random']['efficiency']:.3f}"
    )
    st.text(
        f"Execution Time: {result['random']['time']} sec"
    )

    st.markdown("### Genetic Algorithm")
    st.text(
        f"Efficiency: {result['genetic']['efficiency']:.3f}"
    )
    st.text(
        f"Execution Time: {result['genetic']['time']} sec"
    )

    best = max(
        [
            ("Greedy", result["greedy"]["efficiency"]),
            ("Random", result["random"]["efficiency"]),
            ("Genetic", result["genetic"]["efficiency"])
        ],
        key=lambda x: x[1]
    )

    st.success(
        f" Best Algorithm: {best[0]} | Efficiency: {best[1]:.3f}"
    )

    st.subheader(" Raw Results")

    st.code(
        str(result),
        language="python"
    )