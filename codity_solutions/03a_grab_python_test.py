# The code I submitted for the grab codity python test. It scored 100 on
# correctness but only 33 for performance. Using a dictionary will probably
# make the process faster for large datasets. The objective is to return the
# number of times the eltters for balloon may be removed from a string.
S = 'BAOOLLNNOLOLGBAX'


def solution(S, count=0):
    letters = ['B', 'A', 'L', 'L', 'O', 'O', 'N']
    ls = list(S)
    for l in letters:
        try:
            ls.remove(l)
        except ValueError:
            return count
    count += 1
    return solution(ls, count)


print(solution(S))
