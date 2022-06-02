def check_level(level):
    try:
        level = int(level)
        if type(level) == int and level in range(1, 4):
            return int(level)
    except ValueError:
        return None

