candies = [2,3,5,1,3]
extraCandies = 3

max_candies = max(candies)

result = []

for i in candies:
    result.append(i + extraCandies >= max_candies)

print(result)