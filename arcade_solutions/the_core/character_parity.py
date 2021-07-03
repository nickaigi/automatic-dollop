def character_parity(s):
    return "not a digit" if not s.isdigit() else "odd" if int(s) % 2 else "even"


def character_parity_old(s):
    if s.isdigit():
        n = int(s)
        return "even" if n % 2 == 0 else "odd"
    return "not a digit"
