class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


stk = Stack()


print(stk.isEmpty())
stk.push(1)
stk.push(2)
print(stk.pop())
print(stk.isEmpty())
print(stk.pop())
