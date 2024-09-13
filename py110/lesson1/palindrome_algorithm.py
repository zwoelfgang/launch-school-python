"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string. Palindrome detection
should be case-sensitive.
"""

def palindrome_substrings(string):
    subs = set()
    lst = []

    for idx2 in range(len(string) + 1):
        substring = string[idx2:]
        for idx in range(len(substring) + 1):
            if len(substring[:idx]) > 1:
                subs.add(substring[:idx])

    for el in subs:
        if el == el[::-1]:
            lst.append(el)

    return lst


# Test cases:

# Comments show expected return values
print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]