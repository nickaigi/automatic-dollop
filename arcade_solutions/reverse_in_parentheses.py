def reverse_in_parentheses(str_):
    if str_ == '' or str_ == '()':
        return ''
    str_stack = []
    reverse_stack = []
    found_start, found_stop = False, False
    for i, c in enumerate(str_):
        if c == '(':
            found_start = True
        elif c == ')':
            found_stop = True
        if found_start and not found_stop:
            reverse_stack.append(c)
    print(reverse_stack[1:])
