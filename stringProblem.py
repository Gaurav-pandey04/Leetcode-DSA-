chars = 'Hello World!'
string = ''
alphabets = []
# for char in chars:
#     string += char

for char in chars:
    alphabets.append(char)

string = ''.join(alphabets)

print(string)
print(string == chars)