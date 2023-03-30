class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def get_value(self):
        return self.__value

    next = property(get_next, set_next)
    value = property(get_value)


class LinkList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    # 头插入
    def add(self, value):
        node = Node(value)
        if self.__length:
            node.next = self.__head
            self.__head = node
        else:
            self.__head = self.__tail = node
        self.__length += 1

    # 尾插入
    def append(self, value):
        node = Node(value)
        if self.__length:
            self.__tail.next = node
            self.__tail = node
        else:
            self.__head = self.__tail = node
        self.__length += 1

    # 中间插入
    def insert(self, elem, value):
        if self.__length:
            if self.__head == elem:
                self.add(value)
                return
            else:
                temp = self.__head
                while temp.next:
                    if temp.next == elem:
                        node = Node(value)
                        node.next = elem
                        temp.next = node
                        self.__length += 1
                        return
        print("无法找到指定元素")

    # 删除元素
    def remove(self, elem):
        if self.__head:
            if self.__head == elem:
                self.__head = self.__head.next
                self.__length -= 1
                return
            else:
                temp = self.__head
                while temp.next:
                    if temp.next == elem == self.__tail:
                        temp.next = None
                        self.__tail = temp
                        self.__length -= 1
                        return
                    if temp.next == elem:
                        temp.next = temp.next.next
                        self.__length -= 1
                        return
                    temp = temp.next
                print("无法找到指定元素")


    def items(self):
        temp = self.__head
        while temp:
            yield temp
            temp = temp.next
