def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
        
    L = len(A) - 1
    
    for i in range(K):
        temp = A[L]
        A = A[:L]
        A.insert(0,temp)
        
    return A
