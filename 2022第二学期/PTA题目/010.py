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


def permutations(n):
    stack = Stack()
    stack.push([])
    while not stack.is_empty():
        if len(temp := stack.pop()) != n:
            for i in range(n, 0, -1):
                if i not in temp:
                    stack.push(temp + [i])
        else:
            print(*temp, "")


if __name__ == '__main__':
    permutations(int(input()))
