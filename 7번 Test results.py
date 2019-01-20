def solution(S):
    stack = []
    for i in range(len(S)):
        if S[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
            
    if len(stack) == 0:
        return 1
    else:
        return 0
