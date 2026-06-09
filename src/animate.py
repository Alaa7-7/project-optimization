import numpy as np
import plotly.graph_objects as go

u = np.loadtxt("results/final_result.txt")
x = np.linspace(0, 1, len(u))

fig = go.Figure(
    data=[
        go.Scatter(
            x=x,
            y=u,
            mode="lines"
        )
    ]
)

fig.update_layout(
    title="Advection-Diffusion Final Profile",
    xaxis_title="Position",
    yaxis_title="Concentration"
)

fig.write_html("results/profile.html")
print("Saved: results/profile.html")