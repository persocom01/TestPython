# Longest chain of zeroes in a binary number.
import re

A = "{0:b}".format(3703307)


def solution(A):
    pattern = r'[^0](0+)[^0]'
    matches = re.findall(pattern, A)
    max_len = 0
    for m in matches:
        if len(m) > max_len:
            max_len = len(m)
    return max_len


print(solution(A))
