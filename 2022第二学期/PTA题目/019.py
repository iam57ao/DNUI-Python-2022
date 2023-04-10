class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.lc = None
        self.rc = None

    def pre(self):
        result = []

        def get_pre(node):
            if not node:
                return None
            print(node.data, end=" ")
            get_pre(node.lc)
            get_pre(node.rc)

        get_pre(self)


if __name__ == '__main__':
    tree = [0]
    lst = list(input())
    tree.extend(lst)


    def set_tree(lst_tree, index=1):
        if index > len(tree) - 1 or lst_tree[index] == "#":
            return None
        node = TreeNode(lst_tree[index])
        node.lc = set_tree(lst_tree, index * 2)
        node.rc = set_tree(lst_tree, index * 2 + 1)
        return node


    link_tree = set_tree(tree)
    print("先序序列:", end=" ")
    link_tree.pre()
