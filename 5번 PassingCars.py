def solution(A):
    # write your code in Python 3.6
    pairsCount = 0
    pairsSum = 0
    for i in range(len(A)):
        if A[i] == 0:
            pairsCount += 1
        else:
            pairsSum += pairsCount
    if pairsSum > 1000000000:
        return -1
    else:
        return pairsSum
