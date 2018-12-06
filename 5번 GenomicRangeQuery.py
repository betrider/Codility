def solution(S, P, Q):
    # write your code in Python 3.6
    resultArr = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            resultArr.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            resultArr.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            resultArr.append(3)
        elif 'T' in S[P[i]:Q[i]+1]:
            resultArr.append(4)
    return resultArr
