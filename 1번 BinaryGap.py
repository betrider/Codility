import re

def solution(N):
    # write your code in Python 3.6
    N = bin(N)
    N = N.replace('010','0110')
    Obj = re.findall('10+1',N)
    
    if len(Obj) == 0:
        return 0
    else:
        return len(min(Obj))-2
