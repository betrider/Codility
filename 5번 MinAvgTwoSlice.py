import sys

def solution(A):
    # write your code in Python 3.6
    
    minValue = sys.maxsize
    sLocation = 0
    
    for i in range(len(A)-1):
        if (A[i]+A[i+1])/2 < minValue:
            minValue = (A[i]+A[i+1])/2
            sLocation = i
        if i < len(A)-2:    
            if (A[i]+A[i+1]+A[i+2])/3 < minValue:
                minValue = (A[i]+A[i+1]+A[i+2])/3
                sLocation = i
    
    return sLocation
