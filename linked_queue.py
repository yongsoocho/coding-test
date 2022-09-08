class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def isEmpty(self):
        return not self.head


lq = LinkedQueue()

print(__name__)
print(lq.isEmpty())
lq.enqueue(1)
lq.enqueue(2)
print(lq.dequeue())
print(lq.dequeue())
print(lq.isEmpty())
