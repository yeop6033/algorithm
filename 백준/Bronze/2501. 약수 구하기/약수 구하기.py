a,b = map(int,input().split())
num_list=[]
cnt=1
while cnt<=a:
    if a%cnt==0:
        num_list.append(cnt)
        cnt+=1
    else:
        cnt+=1
if len(num_list)<b:
    print(0)
else:
    print(num_list[b-1])    

            
