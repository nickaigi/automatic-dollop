MONTHS = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
def metro_card(n):
    result = set()
    for i in range(len(MONTHS) - 1):
        if n == MONTHS[i]:
            result.add(MONTHS[i + 1])
    return sorted(list(result))
