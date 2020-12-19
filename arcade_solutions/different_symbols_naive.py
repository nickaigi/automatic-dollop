def different_symbols_naive(s):
    symbols = set()
    for ch in s:
        symbols.update(ch)
    return len(symbols)

def different_symbols_naive_short(s):
    return len(set(s))
