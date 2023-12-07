class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def __getitem__(self, key):
        index = hash(key) % self.size
        entry = self.table[index]
        while entry is not None:
            if entry[0] == key:
                return entry[1]
            index = (index + 1) % self.size
            entry = self.table[index]
        raise KeyError(key)

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def __delitem__(self, key):
        index = hash(key) % self.size
        entry = self.table[index]
        while entry is not None:
            if entry[0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            entry = self.table[index]
        raise KeyError(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        count = 0
        for entry in self.table:
            if entry is not None:
                count += 1
        return count


hash_table = HashTable()
hash_table['one'] = 1
hash_table['two'] = 2
hash_table['three'] = 3

print('Length:', len(hash_table))
print('Contains "two":', 'two' in hash_table)
print('Contains "four":', 'four' in hash_table)