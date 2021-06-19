def number_of_clans(divisors, k):
    return len(
        set(
            [tuple([x%y==0 for y in divisors]) for x in range(1, k+1)]
        )
    )
