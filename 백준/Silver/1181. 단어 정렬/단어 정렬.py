N=int(input())
cat_list=[]
for i in range(N):
    cat_s=input()
    if cat_s not in cat_list:
        cat_list.append(cat_s)
    # print(cat_list)
cat_list.sort()
cat_list.sort(key=len)
for k in cat_list:
    print(k)
