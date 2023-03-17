class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, element):
        self.data.append(element)
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        self.length -= 1
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]


def is_perfect(text):
    stack = Stack()
    for i in text:
        if i == "(":
            stack.push(i)
        else:
            if stack.is_empty():
                return "NO"
            else:
                temp = stack.pop()
                if temp == "(":
                    continue
                return "NO"
    if stack.is_empty():
        return "YES"
    return "NO"


if __name__ == '__main__':
    from sys import stdin

    for j in stdin.read().split():
        print(is_perfect(j))
