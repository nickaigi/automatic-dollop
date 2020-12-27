def build_palindrome(st):
    for i in range(0, len(st)):
        if st[i:len(st)] == st[i:len(st)][::-1]:
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]



def build_palindrome_two(st):
    string_list = list(st)
    i = 0
    while string_list != string_list[::-1]:
        string_list.insert(len(st), st[i])
        i += 1
    return ''.join(string_list)

if __name__ == '__main__':
    st = 'abcdc'
    print(f'{st} -> {build_palindrome_two(st)}')
    st = 'ababab'
    print(f'{st} -> {build_palindrome_two(st)}')
    st = 'abc'
    print(f'{st} -> {build_palindrome_two(st)}')
