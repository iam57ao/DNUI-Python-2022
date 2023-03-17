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
    level = "<([{>)]}"
    stack = Stack()
    for i in text:
        if i in "<([{":
            if stack.is_empty() or level.index(i) <= level.index(stack.peek()):
                stack.push(i)
            else:
                return "NO"
        else:
            if stack.is_empty():
                return "NO"
            temp = stack.pop()
            if level.index(i) - level.index(temp) == 4:
                continue
            return "NO"
    if stack.is_empty():
        return "YES"
    return "NO"


if __name__ == '__main__':

    for j in range(int(input())):
        user_input = input()
        print(is_perfect(user_input))
