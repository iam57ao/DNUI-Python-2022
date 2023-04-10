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
    elem_num = int(input())
    elem = input().split(" ")
    elem_dict = dict()
    for i in elem:
        elem_dict[i] = TreeNode(i)
    from sys import stdin

    for j in stdin.readlines():
        line = j.strip().split(" ")
        if line[1] == "1":
            elem_dict[line[0]].lc = elem_dict[line[2]]
        else:
            elem_dict[line[0]].rc = elem_dict[line[2]]
    print(elem_dict["A"].get_height())
