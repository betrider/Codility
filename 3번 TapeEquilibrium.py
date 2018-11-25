import math
import sys

def solution(A):
    # write your code in Python 3.6
    sumA = 0
    sumB = sum(A)
    difference = sys.maxsize
    
    for i in range(1,len(A),1):
        sumA += A[i-1]
        sumB -= A[i-1]
        if abs(sumA - sumB) < difference:
            difference = abs(sumA - sumB)
        
    return difference
