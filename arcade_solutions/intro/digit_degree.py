def digit_degree(n):
    if n < 10:
        return 0
    else:
        return 1 + digit_degree(sum([int(ch) for ch in str(n)]))

if __name__ == '__main__':
   x = digit_degree(5)
   print(x)
   x = digit_degree(91)
   print(x)
