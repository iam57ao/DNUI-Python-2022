for count in range(int(input())):
    n = int(input())
    out_list = [[0 for i in range(n)] for j in range(n)]
    if n % 2 != 0:  # 判断是否为奇数
        out_list[n // 2][n // 2] = 1  # 如果是奇数，中间放入1
    for level in range(n // 2):  # 层数循环
        for right in range(n - 1 - 2 * level):  # 同层向右
            out_list[level][right + level] = (n - 2 * level) ** 2 - right
        for left in range(n - 1 - 2 * level):  # 同层向左
            out_list[n - 1 - level][n - 1 - level - left] = (n - 1 - 2 * level) ** 2 + 1 - left
        for up in range(n - 1 - 2 * level):  # 同层向上
            out_list[up + 1 + level][level] = (n - 2 * (level + 1)) ** 2 + 1 + up
        for down in range(n - 1 - 2 * level):   # 同层向下
            out_list[down + level][n - 1 - level] = (n - 2 * level) ** 2 - (n - 1 - 2 * level) - down
    for out in out_list:
        for num in out:
            print(f"{num}".rjust(4, " "), end="")
        print()
