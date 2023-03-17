class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = Node(val)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def difference(self, link_list):
        cur = None
        cur1 = self.head
        cur2 = link_list.head
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur = cur1
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                cur2 = cur2.next
            else:
                if cur:
                    cur.next = cur1.next
                    cur1 = cur.next
                    if cur1 is None:
                        self.tail = cur
                else:
                    self.head = cur1.next
                    cur1 = self.head
                cur2 = cur2.next
        self.all()

    def all(self):
        cur = self.head
        while cur:
            if cur == self.tail:
                print(cur.val)
            else:
                print(cur.val, end=" ")
            cur = cur.next


if __name__ == '__main__':
    for i in range(int(input())):
        l1 = LinkList()
        l2 = LinkList()
        for j in list(map(int, input().split()))[1:]:
            l1.append(j)
        for k in list(map(int, input().split()))[1:]:
            l2.append(k)
        l1.difference(l2)
