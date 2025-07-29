nums1 = [1, 2]
nums2 = [3]

num3 = nums1 + nums2
num3.sort()
median = 0
if(len(num3)%2 == 0):
    left = (len(num3) // 2) -1
    right = (len(num3) // 2) 
    print(num3[left], num3[right])
    median = (num3[left]+num3[right])
    median /= 2
else:
    median = num3[len(num3)//2]

print(median)