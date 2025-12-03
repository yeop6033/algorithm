S = input()
set_S = []

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        # print(substring)
        set_S.append(substring)

print(len(set(set_S)))
