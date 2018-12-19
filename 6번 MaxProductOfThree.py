def solution(A):
    # write your code in Python 3.6
    A.sort()
    lenArr = len(A)
    if A[lenArr-1]*A[0]*A[1] > A[lenArr-1]*A[lenArr-2]*A[lenArr-3]:
        return A[lenArr-1]*A[0]*A[1]
    else:
        return A[lenArr-1]*A[lenArr-2]*A[lenArr-3]
