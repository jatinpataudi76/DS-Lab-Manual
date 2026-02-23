# Stack ADT using list

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)
        print(x, "pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# testing
s = Stack()
s.push(10)
s.push(20)
print("Top =", s.peek())
print("Pop =", s.pop())
print("Size =", s.size()) 