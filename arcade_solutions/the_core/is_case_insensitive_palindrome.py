def is_case_insensitive_palindrome(s):
    return s.lower() == s[::-1].lower()
