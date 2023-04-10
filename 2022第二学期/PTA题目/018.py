class TreeNode:
    def __init__(self, data=None):
        self.lc = None
        self.rc = None
        self.data = data

    def post(self):
        result = []

        def get_post(node):
            if not node:
                return

            get_post(node.lc)
            get_post(node.rc)
            result.append(node.data)

        get_post(self)
        return result


total = int(input())
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
print("".join(result_node.post()))
