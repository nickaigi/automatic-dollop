def elections_winners_soln(votes, k):
    m = max(votes)
    if k == 0:
        return 1 if len([v for v in votes if v == m]) == 1 else 0
    return len([v for v in votes if v + k > m])


def elections_winners(votes, k):
    count = 0
    for i, v in enumerate(votes):
        if v + k > max(votes[0:i] + votes[i+1:]):
            count += 1
    return count


if __name__ == '__main__':
    votes = [2, 3, 5, 2]
    k = 3
    print(elections_winners(votes, k))
