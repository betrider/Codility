def solution(A):
    # write your code in Python 3.6
    num = 1
    A.sort()
    for i in range(len(A)):
        if A[i] == num:
            num += 1
    return num
