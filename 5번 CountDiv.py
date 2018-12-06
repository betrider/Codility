def solution(A, B, K):
    # write your code in Python 3.6
    revision = 0
    if A==0:
        revision = 1

    return int(B/K)-int((A-1+revision)/K)+revision
