class TreeNode:
    def __init__(self, data=None):
        self.lc = None
        self.rc = None
        self.data = data

    def get_height(self):
        def find(node):
            if not node:
                return 0
            l_height = 1 + find(node.lc)
            r_height = 1 + find(node.rc)
            return max(l_height, r_height)

        return find(self)


if __name__ == '__main__':

    pre = list(input())
    mid = list(input())


    def set_tree(node, new_pre, new_mid):
        if not new_mid:
            return None
        node.data = new_pre[0]
        node.lc = set_tree(TreeNode(), [i for i in new_pre if i in new_mid[:new_mid.index(new_pre[0])]],
                           new_mid[:new_mid.index(new_pre[0])])
        node.rc = set_tree(TreeNode(), [i for i in new_pre if i in new_mid[new_mid.index(new_pre[0]) + 1:]],
                           new_mid[new_mid.index(new_pre[0]) + 1:])
        return node


    result_node = set_tree(TreeNode(), pre, mid)
    print(result_node.get_height())
