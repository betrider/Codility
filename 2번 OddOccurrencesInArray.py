def solution(A):
    # write your code in Python 3.6
    result = 0
    for i in A:
        result ^= i
    return result
