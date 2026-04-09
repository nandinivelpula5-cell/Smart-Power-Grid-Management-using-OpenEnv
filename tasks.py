def load_task(level):
    if level == "easy":
        return {"num_areas": 3, "complaints": 2}
    elif level == "medium":
        return {"num_areas": 5, "complaints": 5}
    elif level == "hard":
        return {"num_areas": 10, "complaints": 10}
    else:
        raise ValueError("Invalid task level")