def solution(S):
    # write your code in Python 3.6
    stack = []
    
    for chr in S:
        if chr == "{" or chr == "[" or chr == "(":
            stack.append(chr)
        else:
            if len(stack) == 0:
                return 0
            stackLast = stack[-1]
            if chr == "}" and stackLast == "{":
                stack.pop()
            elif chr == "]" and stackLast == "[":
                stack.pop()
            elif chr == ")" and stackLast == "(":
                stack.pop()
            else:
                return 0
            
    if len(stack) > 0:
        return 0
    else:
        return 1
