class TreeNode:
    def __init__(self, data=None):
        self.lc = None
        self.rc = None
        self.data = data

    def pre(self):
        result = []

        def get_pre(node):
            if not node:
                return
            result.append(node.data)
            get_pre(node.lc)
            get_pre(node.rc)

        get_pre(self)
        return result


total = int(input())
post = list(map(int, input().split()))
mid = list(map(int, input().split()))


def set_tree(node, new_post, new_mid):
    if not new_mid:
        return None
    node.data = new_post[-1]
    node.lc = set_tree(TreeNode(), [i for i in new_post if i in new_mid[:new_mid.index(new_post[-1])]],
                       new_mid[:new_mid.index(new_post[-1])])
    node.rc = set_tree(TreeNode(), [i for i in new_post if i in new_mid[new_mid.index(new_post[-1]) + 1:]],
                       new_mid[new_mid.index(new_post[-1]) + 1:])
    return node


result_node = set_tree(TreeNode(), post, mid)
print("Preorder:", *result_node.pre())
