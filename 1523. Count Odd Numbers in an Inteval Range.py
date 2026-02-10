low = int(input("Enter a integer 1: "))
high = int(input("Enter a interger 2: "))
even = []
odd = []
for i in range(low, high + 1):
    if i % 2 == 0:
        even.append(i)
    
    elif i % 2 != 0:
        odd.append(i)

    else:
        print("Please enter a valid number")

print(len(odd))


# With less complexity
high = 8
low = 2
print((high + 1) // 2 - low // 2)