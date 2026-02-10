n = 234
prod = 1
sum = 0
temp = n

while temp > 0:
    digits = temp % 10
    prod = digits * prod
    sum = sum + digits
    temp //= 10 

difference = prod - sum
print(difference)
