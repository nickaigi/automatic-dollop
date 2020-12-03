def reverse_in_parentheses(s):
    for i in range(len(s)):
        if s[i] == '(':
            start = i
        if s[i] == ')':
            end = i
            return reverse_in_parentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

if __name__ == '__main__':
    s = '(bar)'
    print(reverse_in_parentheses(s))
    print(reverse_in_parentheses('foo(bar(baz))blim'))
    print(reverse_in_parentheses('(abc)d(efg)'))
