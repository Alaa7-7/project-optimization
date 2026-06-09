def solve_exact(request):
    size = request.get("size", 10)

    result = {
        "selected_items": list(range(size)),
        "cost": size * 10
    }

    return result