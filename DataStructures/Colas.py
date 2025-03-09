from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    def is_empty(self):
        return len(self.queue) == 0
    def view(self):
        return[i for i in self.queue]

q = Queue()
q.enqueue(10)    
q.enqueue(15)
print(q.view())    
        