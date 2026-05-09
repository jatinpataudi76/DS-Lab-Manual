class HashTable:

    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):

        index = self.hash_function(key)

        self.table[index].append((key, value))

    def search(self, key):

        index = self.hash_function(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return "Not Found"

    def delete(self, key):

        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):

            if k == key:
                del self.table[index][i]
                return

ht = HashTable()

ht.insert(1, "Apple")
ht.insert(11, "Banana")   # collision example

print("Search 1:", ht.search(1))

print("Search 11:", ht.search(11))

ht.delete(1)

print("After Delete:", ht.search(1))