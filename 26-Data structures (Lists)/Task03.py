class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.front.data

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Peek:", queue.peek())

print("Dequeue:", queue.dequeue())
print("Queue size after dequeue:", queue.size())
