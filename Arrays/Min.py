height = [0,2]
n = len(height)
width = 0
min_height = 0
max_value = 1 
for i in range(n):
    for j in range(i+1, n):
        width = j-i
        if height[i]>=height[j]:
            min_height = height[j]
        print(height[i], height[j])
        max_value = max(max_value, min_height*width)
        print("Min Height:", min_height)
        print("Wdith:", width)
        print("Value:", max_value)

print(max_value)