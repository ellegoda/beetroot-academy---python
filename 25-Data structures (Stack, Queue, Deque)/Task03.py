class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        try:
            index = self.items.index(element)
            return self.items.pop(index)
        except ValueError:
            raise ValueError(f"Element {element} not found in the stack")


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise ValueError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        try:
            index = self.items.index(element)
            return self.items.pop(index)
        except ValueError:
            raise ValueError(f"Element {element} not found in the queue")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

try:
    result = stack.get_from_stack(2)
    print(f"Element found and removed from stack: {result}")
except ValueError as ve:
    print(ve)

try:
    result = stack.get_from_stack(4)  # Element not in stack
    print(f"Element found and removed from stack: {result}")
except ValueError as ve:
    print(ve)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

try:
    result = queue.get_from_queue(2)
    print(f"Element found and removed from queue: {result}")
except ValueError as ve:
    print(ve)

try:
    result = queue.get_from_queue(4)
    print(f"Element found and removed from queue: {result}")
except ValueError as ve:
    print(ve)
