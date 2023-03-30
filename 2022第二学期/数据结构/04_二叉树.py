class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root_data=None):
        self.root_data = root_data

    def is_empty(self):
        return not self.root_data

    def preorder(self, data=None):
        if not data:
            return
        print(data.data, end="")
        self.preorder(data.left)
        self.preorder(data.right)

    def inorder(self, data=None):
        if not data:
            return
        self.inorder(data.left)
        print(data.data, end="")
        self.inorder(data.right)

    def postorder(self, data=None):
        if not data:
            return
        self.postorder(data.left)
        self.postorder(data.right)
        print(data.data, end="")




if __name__ == '__main__':
    root = Node("A")
    l2_1 = Node("B")
    r2_2 = Node("C")
    l3_1 = Node("D")
    r3_2 = Node("E")
    l3_3 = Node("F")
    r3_4 = Node("G")
    root.left = l2_1
    root.right = r2_2
    l2_1.left = l3_1
    l2_1.right = r3_2
    r2_2.left = l3_3
    r2_2.right = r3_4
    tree = Tree(root)
    tree.preorder(tree.root_data)
    print()
    tree.inorder(tree.root_data)
    print()
    tree.postorder(tree.root_data)