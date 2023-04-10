class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __del__(self):
        while self.head:
            node = self.head
            self.head = node.next
            del node

    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            print("队列为空")
            return
        node = self.head
        self.head = node.next
        self.length -= 1

    def front(self):
        if not self.is_empty():
            return self.head
        return None
