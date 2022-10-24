price = int(input())
identity = input()
if identity == "学生":
    print(f"请支付{price * 0.8:.2f}元现金购买一张门票")
else:
    print(f"请支付{price:.2f}元现金购买一张门票")
