def reach_next_level(xp, threshold, reward):
    return xp + reward >= threshold


if __name__ == '__main__':
    xp = 10
    threshold = 15
    reward = 5
    reach_next_level(xp, threshold, reward)
