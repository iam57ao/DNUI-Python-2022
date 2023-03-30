class Stack:
    def __init__(self):
        self.stack = []

    def __del__(self):
        while self.stack:
            del self.stack[-1]

    def is_empty(self):
        return not self.stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
