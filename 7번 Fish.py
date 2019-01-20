def solution(A, B): 
    
    upStack = []
    downStack = []
        
    for fish in range(len(A)):
        if B[fish] == 0:
            if len(downStack) > 0:
                for stream in range(len(downStack)-1,-1,-1):
                    if A[fish] > downStack[stream]:
                        downStack.pop()
                    else:
                        break
                    if len(downStack) == 0:
                        upStack.append(A[fish])
            else:
                upStack.append(A[fish])
        else: #1
            downStack.append(A[fish])
        
    return len(upStack)+len(downStack)
