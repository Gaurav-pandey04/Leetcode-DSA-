'''
    Let's evaluate the balanicng of symbol problem 
    Step 1: Use a Stack (List with Top pointer)
    Step 2: Append the starting symbol
    Step 3: If closing symbol encounter then
                    remove the symbol from stack
    Step 4: If closing Symbol encounter and Stack is empty then 
                    Raise Exception
    Step 5: If end then check the Stack is empty if not 
                    Raise Exception    
'''

expression = '[(A+B)/(C+D)]'
top = 0
symbol = []
sym = {
    ']':'[',
    ')':'(',
    '}':'{'
}
starting_sym = ['[','(','{']
closing_sym = [']',')','}']
for exp in expression:
    if exp in starting_sym:
        symbol.append(exp)
        top += 1
    if exp in closing_sym:
        if sym[exp] == symbol[-1]:
            del symbol[-1]
        else:
            print("Exception")

    print(symbol)