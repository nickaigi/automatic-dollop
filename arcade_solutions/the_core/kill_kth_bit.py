def kill_kth_bit(n,k):
    bin_n = str(bin(n)[2:])
    result = ''
    for i in range(len(bin_n)):
        if i == k:
            result += '0'
        else:
            result += bin_n[i]

    print(int(result, 2))

if __name__ == '__main__':
    n = 37
    k = 3
    kill_kth_bit(n, k)
