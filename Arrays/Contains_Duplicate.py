nums = [1,2,3,4]

set_nums = set()

def check(nums):
    for num in nums:
        if num in set_nums:
            return True
        else:
            set_nums.add(num)

    return False

print(check(nums))