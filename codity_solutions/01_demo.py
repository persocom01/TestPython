# Return smallest integer not found in list.
A = [1, 3, 6, 4, 1, 2]


def solution(A):
    a_set = set(A)
    for i in range(1, 1000001):
        if i not in a_set:
            return i


print(solution(A))
