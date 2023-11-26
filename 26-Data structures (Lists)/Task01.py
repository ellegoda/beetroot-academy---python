class Node:
    def __init__(self, init_data) -> None:
        self.data = init_data
        self.next = None


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        return self.size()

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def append(self, item):
        self.add(item)

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not in list")

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")

        current = self.head
        previous = None
        index = 0

        while index < pos:
            previous = current
            current = current.next
            index += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("insert index out of range")

        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            index = 0

            while index < pos:
                previous = current
                current = current.next
                index += 1

            temp = Node(item)
            previous.next = temp
            temp.next = current

    def slice(self, start, stop):
        if start < 0 or stop > self.size() or start >= stop:
            raise ValueError("Invalid start or stop parameters")

        current = self.head
        index = 0
        result = UnorderedList()

        while index < stop:
            if start <= index < stop:
                result.append(current.data)
            current = current.next
            index += 1

        return result


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.add(5)
    my_list.append(6)

    print("Index of 3:", my_list.index(3))
    print("Pop at position 2:", my_list.pop(2))
    print("Insert 10 at position 1:", my_list.insert(1, 10))
    print("Slice from position 1 to 4:", my_list.slice(1, 4))