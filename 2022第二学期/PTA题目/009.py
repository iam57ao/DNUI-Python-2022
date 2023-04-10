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


def calculate(text):
    stack = Stack()
    for i in text:
        if i.isdigit():
            stack.push(i)
        else:
            if stack.length < 2 or i not in "+-*/":
                print("Expression Error!")
                return
            a, b = stack.pop(), stack.pop()
            try:
                stack.push(int(eval(f"{b}{i}{a}")))
            except ZeroDivisionError:
                print("Division By Zero!")
                return
    if stack.length == 1:
        print(stack.pop())
    else:
        print("Expression Error!")


if __name__ == '__main__':
    for j in range(int(input())):
        calculate(input())
