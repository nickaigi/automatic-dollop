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
