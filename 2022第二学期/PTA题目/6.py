class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        raise IndexError


if __name__ == '__main__':
    from sys import stdin


    def is_perfect(text):
        stack = Stack()
        try:
            for i in text:
                if i == "(":
                    stack.push(i)
                else:
                    stack.pop()
        except IndexError:
            return "NO"
        else:
            if stack.is_empty():
                return "YES"
            return "NO"


    for i in stdin.read().split():
        print(is_perfect(i))
