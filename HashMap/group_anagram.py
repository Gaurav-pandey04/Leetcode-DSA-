strs = ["eat","tea","tan","ate","nat","bat"]

visited = set()
output = []

for i in range(len(strs)):
    anagrams = [strs[i]] if i not in visited else []

    visited.add(i)

    for j in range(i, len(strs)):
        if sorted(strs[i]) == sorted(strs[j]) and j not in visited:
            anagrams.append(strs[j])
            visited.add(j)
    
    if len(anagrams)>=1:
        output.append(anagrams)

print(output)


# another optimised approach 

from collections import defaultdict

output = defaultdict(list)

for s in strs:
    key = "".join(sorted(s))
    output[key].append(s)

print(list(output.values()))