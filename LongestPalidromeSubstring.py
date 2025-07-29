# Leetcode probelm - Done

s = "baabad"
n = len(s)
start = 0
max_len = 1
if n==0:
    print('')
for i in range(n):
    for j in range(i, n):
        substring = s[i:j+1]
        if substring == substring[::-1]:
            if j-i+1>max_len:
                max_len = j-i+1
                start = i

print(s[start: start+max_len])