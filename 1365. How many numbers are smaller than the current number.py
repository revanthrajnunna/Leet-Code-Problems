n = [8,1,2,2,3]

ans = []

for i in n:
    count = 0
    for j in n:
        if i > j:
            count+=1
    ans.append(count)

print(ans)

