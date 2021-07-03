def character_parity(symbol):
    if symbol.isdigit():
        n = int(symbol)
        return "even" if n % 2 == 0 else "odd"
    return "not a digit"
