class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            pop_val = self.head.data
            self.head = self.head.next
            return pop_val

    def top(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.head.data

    def isEmpty(self):
        return not self.head


ls = LinkedStack()

print(ls.isEmpty())
ls.push(1)
ls.push(2)
ls.push(3)
print(ls.isEmpty())
print(ls.top())
print(ls.pop())
print(ls.top())
print(ls.pop())
print(ls.top())
print(ls.pop())
print(ls.top())
print(ls.isEmpty())
