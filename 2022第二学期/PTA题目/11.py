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


def is_perfect(text):
    stack = Stack()
    for i in text:
        if i in "[{(":
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            temp = stack.pop()
            if temp == "(" and i == ")" or temp == "[" and i == "]" or temp == "{" and i == "}":
                continue
            return False
    if stack.is_empty():
        return True
    return False


if __name__ == '__main__':
   for j in range(int(input())):
       print("Yes" if is_perfect(input()) else "No")