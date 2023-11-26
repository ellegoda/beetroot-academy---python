class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.top.data

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Peek:", stack.peek())

print("Pop:", stack.pop())
print("Stack size after pop:", stack.size())
