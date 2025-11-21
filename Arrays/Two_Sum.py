nums = [3,2,4]
target = 6

def check(nums, target):
    l = 0
    r = 1
    while r < len(nums):
        if nums[l]+nums[r] == target:
            return ([l, r])
        if nums[l]+nums[r] > target:
            r += 1
        if nums[l]+nums[r] > target:
            l += 1


print(check(nums, target))