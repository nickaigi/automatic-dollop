def makeArrayConsecutive2(statues):
    statues.sort()
    missing = range(statues[0], (statues[-1] + 1))
    import pdb; pdb.set_trace()
    return len(missing) - len(statues)


if __name__ == '__main__':
    statues = [6, 2, 3, 8]
    print(makeArrayConsecutive2(statues))
