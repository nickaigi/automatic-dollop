def election_winners(votes, k):
    max_v = max(votes)
    winners = 0

    if k == 0 and votes.count(max_v) == 1:
        return 1
    for v in votes:
        if v + k > max_v:
            winners += 1
    return winners


if __name__ == '__main__':
    votes = [2, 3, 5, 2]
    k = 3
    soln = election_winners(votes, k)
    print(soln)
