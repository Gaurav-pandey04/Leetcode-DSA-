# Leetcode - Delete Charachter to make string fancy
# Done - All test cases passed
s = 'aabaabaabaa'
counter = []
new_s = ' '
prev_char = ''
isremoved = False
for char in s:
    if char == prev_char:
        counter.append(char)
    if len(counter) >= 2 and char in counter:
        isremoved = True
        continue
    if isremoved or char not in counter:
        counter = []
        isremoved = False
    new_s += char 
    prev_char = char

print(new_s)