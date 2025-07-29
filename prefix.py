strs = ["flower","flow","flight"]

i, j = 0, 1
k, l, m = 0, 0, 0
result = []

string = strs[0]

if len(strs) == 1:
    print(string)

for i in range(1, len(strs)):
    while  k < len(string) and l < len(strs[i]):
        print(string, strs[i])
        if string[k] == strs[i][l] and string[k] not in result:
            result.append(strs[i][l])
        if string[k] != strs[i][l] and string[k] in result:
            result.remove(string[k])
            print(result)
        k += 1
        l += 1

        
print(''.join(result))