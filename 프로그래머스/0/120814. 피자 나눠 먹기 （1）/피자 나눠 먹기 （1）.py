def solution(n):
    p_num=0
    if n//7<=1:
        p_num=1
    elif n%7==0:
        p_num=n//7
    else:
        p_num=(n//7)+1
        
    return p_num