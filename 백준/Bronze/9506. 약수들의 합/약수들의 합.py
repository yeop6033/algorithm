while True:
    a= int(input())    
    if a== -1:
        break
    num=0
    list_num=[]

    for i in range(1,a):
        if a%i ==0:
            num=num+i
            list_num.append(i)
    if num == a:
        print(f"{a} = {' + '.join(map(str, list_num))}")
    else:
        print(f"{a} is NOT perfect.")