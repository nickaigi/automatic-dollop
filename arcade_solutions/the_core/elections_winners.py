def elections_winners(votes, k):
    count = 0
    if k == 0 and votes.count(max(votes)) == 1:
        return 1

    for i, v in enumerate(votes):
        temp = votes.copy()
        temp[i] = v + k
        if temp.count(max(temp)) == 1:
            count += 1
    return count


if __name__ == '__main__':
    votes = [2, 3, 5, 2]
    k = 3
    print(elections_winners(votes, k))
