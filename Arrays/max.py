nums = [4,6,5,8]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

j = 1
k = 1
for num in nums[:k]:
    prime = is_prime(num)
    print(num)
    if prime:
        for n in nums[:j+1]:
            print(n)
            if n % num == 0:
                k += 1
        print(k)
        j += 1
        break
    j += 1

print(j)