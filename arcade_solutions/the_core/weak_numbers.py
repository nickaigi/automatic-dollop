def weak_numbers(n):
    factors = [count_factors(n) for n in range(1, n+1)]
    weaknesses = []
    for num, num_factors in enumerate(factors, 1):
        weakness = 0
        for factor in factors[:num]:
            if factor > num_factors:
                weakness += 1
        weaknesses.append(weakness)
    weakest = max(weaknesses)
    return [weakest, weaknesses.count(weakest)]


def count_factors(n):
    _factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            _factors += 1
    return _factors
