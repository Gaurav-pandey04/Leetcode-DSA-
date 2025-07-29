s = 'dvdf'
char = []
string = ''
max = 0
for i in s:
    if (i not in string):
        string +=i
        # print(string)
    else:
        char.append(string)
        string = ''+i

if string:
    char.append(string)

for strg in char:
    print(strg)
    if(len(strg) > max):
        max = len(strg)

print(max)