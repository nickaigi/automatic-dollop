def knapsack_light(v1, w1, v2, w2, max_weight):
    if w1 + w2 <= max_weight:
        return v1 + v2
    elif w1 > max_weight and w2 > max_weight:
        return 0
    elif w1 > max_weight:
        return v2
    elif w2 > max_weight:
        return v1
    else:
        return max(v1, v2)


if __name__ == '__main__':
    value1 = 10
    weight1 = 5
    value2 = 6
    weight2 = 4
    max_weight = 8
    #ans = 10
    print(knapsack_light(value1, weight1, value2, weight2, max_weight))
