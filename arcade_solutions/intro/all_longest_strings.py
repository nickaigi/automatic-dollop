def all_longest_strings(input_array):
    max_len = max([len(s) for s in input_array])
    longest = [s for s in input_array if len(s) == max_len]
    return longest
