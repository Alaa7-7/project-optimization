def solve_exact(request):
    size = request.get("size", 10)

    #  Optimization 
    selected = list(range(size))

    cost = sum((i + 1) * 1.5 for i in selected)
    efficiency = round((size * 100) / (cost + 1), 2)

    return {
        "selected_items": selected,
        "cost": round(cost, 2),
        "efficiency_score": efficiency
    }
