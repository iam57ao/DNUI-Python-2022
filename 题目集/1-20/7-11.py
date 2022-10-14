apple = int(input())
print(f"""每人分得{apple // 5}个苹果.
一共分出去{apple - (apple % 5)}个苹果.
交还老师{apple % 5}个苹果.""")
