def solution(n):
    answer=0
    for i in range(2,n,2):
        answer= answer+i
    if n%2==0:
        answer=answer+n
    
    return answer