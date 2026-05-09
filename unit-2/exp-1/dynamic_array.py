class DynamicArray:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if self.data:
            return self.data.pop()
        return "Array Empty"

    def display(self):
        print(self.data)

arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)

arr.display()

arr.pop()

arr.display()