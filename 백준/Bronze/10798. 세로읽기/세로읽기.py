data = [input().strip() for _ in range(5)]
result = ""
for col in range(15):  
    for row in range(5):  
        if col < len(data[row]):  
            result += data[row][col]

print(result)