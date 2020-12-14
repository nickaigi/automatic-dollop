def even_digits_only(n):
    return all([int(x) % 2 == 0 for x in str(n)])

if __name__ == '__main__':
    n = 248622
    print(even_digits_only(n))
    n = 642386
    print(even_digits_only(n))
