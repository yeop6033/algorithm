def solution(array, height):
    num=0
    for i in array:
        if i> height:
            num=num+1
        else:
            num=num
    return num