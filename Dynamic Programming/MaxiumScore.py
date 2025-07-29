s = 'cdbcbbaaabab'
x = 4
y = 5
res = 0
def remove_pair(s, a, b, points):
    stack = []
    score = 0
    for c in s:
        if stack and stack[-1] == a and c==b:
            stack.pop()
            score += points
        else:
            stack.append(c)
            print(stack)
        print(score)
        
    return ''.join(stack), score

if x>=y:
    s, gain = remove_pair(s, 'a', 'b', x)
    res += gain 
    s, gain = remove_pair(s, 'b', 'a', y)
    res += gain
else:
    s, gain = remove_pair(s, 'b', 'a', y)
    res += gain
    s, gain = remove_pair(s, 'a', 'b', x)
    res += gain 

print(res)