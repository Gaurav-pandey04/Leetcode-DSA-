arr = [12, 34, 67, 89, 30]

largest_num = 0
secondLargest_num = 0

for i in range(len(arr)):
    if largest_num < arr[i]:
        secondLargest_num = largest_num
        largest_num = arr[i]

print(secondLargest_num)