class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)         # Add to top 

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()    # Removes from Top
        return None                    # or Raise Exception
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
print(s.size())