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


def is_palindrome(text):
    stack = Stack()
    length = len(text)
    for i in text[:length // 2]:
        stack.push(i)
    for j in text[-(length // 2):]:
        temp = stack.pop()
        if temp == j:
            continue
        return False
    if stack.is_empty():
        return True
    return False


if __name__ == '__main__':
    print(f"{user_input}是回文。" if is_palindrome(user_input := input()) else f"{user_input}不是回文。")
