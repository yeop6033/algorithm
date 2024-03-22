def solution(n, t):
    if t==0:
        answer= n
        return answer;
    else:
        answer=n*(2**t)
        return answer
        
    return answer