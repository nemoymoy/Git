class Stack:
    def __init__(self):
        self.list_elements = list()

    def is_empty(self):
        return len(self.list_elements) == 0

    def push(self, element):
        self.list_elements.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Index out of range")
        else:
            return self.list_elements.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Index out of range")
        else:
            return self.list_elements[-1]

    def size(self):
        return len(self.list_elements)

