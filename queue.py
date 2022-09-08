class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            return self.queue.pop(0)

    def enqueue(self, val):
        self.queue.append(val)

    def isEmpty(self):
        return len(self.queue) == 0


print(__name__)
qu = Queue()
print(qu.isEmpty())
qu.enqueue(1)
qu.enqueue(2)
print(qu.isEmpty())
print(qu.dequeue())
print(qu.dequeue())
print(qu.isEmpty())
