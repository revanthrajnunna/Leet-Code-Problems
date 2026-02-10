n = 4

if n <= 0:
    print(False)
while n % 2 == 0:
    n //= 2

if n == 1:
    print(True)
else:
    print(False)

## With recursion

#base case

def poweroftwo(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False 

#recursive case
    return poweroftwo(n // 2)

print(poweroftwo(16))