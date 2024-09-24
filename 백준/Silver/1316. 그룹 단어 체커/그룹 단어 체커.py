a = int(input())  
count = 0  

for i in range(a):
    b = input()  
    seen = []  
    is_group_word = True  

    for j in range(len(b)):
        if j > 0 and b[j] != b[j - 1]:
            if b[j] in seen:
                is_group_word = False
                break
        seen.append(b[j])

    if is_group_word:
        count += 1  

print(count)
