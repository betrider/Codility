def solution(X, A):
    # write your code in Python 3.6
    chkNum = [False] * X
    sumNum = 0
    for i in range(len(A)):
        if chkNum[A[i]-1] == False:
            chkNum[A[i]-1] = True
            sumNum += 1
        if sumNum == X:
            return i
    return -1
