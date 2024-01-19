class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Przykłady użycia
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # zwraca 2
print(s.pop())  # zwraca 1
