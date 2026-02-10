num = 121
count = 0
temp = num

while temp > 0:
    r = temp % 10
    if num % r == 0:
        count+=1
    temp //= 10

print(count)