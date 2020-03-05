# You are given N counters, initially set to 0, and you have two possible
# operations on them:
# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive
# operations:
# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
N = 5
A = [3, 4, 4, 6, 1, 4, 4]


def solution(N, A):
    arr = [0 for x in range(N)]

    def increase(arr, X):
        arr[X] = arr[X] + 1
        return arr

    def max_counter(arr):
        max_val = max(arr)
        return [max_val for x in range(N)]

    for X in A:
        if 1 <= X <= N:
            arr = increase(arr, X-1)
            print(arr)
        if X == N + 1:
            arr = max_counter(arr)
    return arr
