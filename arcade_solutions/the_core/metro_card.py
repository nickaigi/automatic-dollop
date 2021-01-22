MONTHS = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]


def metro_card(n):
    result = set()
    for i in range(len(MONTHS) - 1):
        if n == MONTHS[i]:
            result.add(MONTHS[i + 1])
    return sorted(list(result))


def metro_card_short(n):
    if n == 31:
        return [28, 30, 31]
    return [31]
