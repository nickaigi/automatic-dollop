def reverse_in_parentheses(str_):
    if str_ == '' or str_ == '()':
        return ''
    str_stack = []
    reverse_stack = []
    found_start, found_stop = False, False
    original_str = []
    for i, c in enumerate(str_):
        if c == '(':
            found_start = True
        elif c == ')':
            found_stop = True
        else:
            str_stack.append(i)
        if found_start and not found_stop:
            reverse_stack.append(c)

    reverse_stack = reverse_stack[1:]  #!+ takes care of leading parentheses
    for i, j in zip(str_stack[:-1], str_stack[1:]):
        if j - 1 == 1:
            original_str.append(str_[i])
    print(''.join(original_str))

    return ''.join(reverse_stack[::-1])  #!+ solves the (bar) == 'rab'
