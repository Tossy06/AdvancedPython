class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
            
        if not  self.is_empty():
            return  self.stack.pop()
        return('Stack is Empty')

    def peek(self):
        if not self.is_empty():
            return self.stack[1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def view(self):
        return [i for i in self.stack]
    
s = Stack()
s.push(5)
s.push(15)
print(s.view())
