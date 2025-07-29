arr = [2, 7, 8, 9, 3, 20]
target = 27

map = {}
result = []
for i, num in enumerate(arr):
    compliment = target - num

    if compliment in map:
        result.append(map[compliment])
        result.append(i)

    map[num] = i

print(result)