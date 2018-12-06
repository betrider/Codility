def solution(A):
    # write your code in Python 3.6
    s = set('')
    for i in range(len(A)):
        s.add(A[i])
    return len(s)
