# 获取键盘上的数据 ——————input(...)
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
#
# print(f"您的姓名是{name}，年龄为{age}")

# 案例：银行卡ATM取款
# 总金额
# total = 10000
#
# #1.输入密码
# password = input("请输入您的银行卡密码：")
# print(f"密码正确，{password}")
#
# #2.输入取款金额
# money = input("请输入您的取款金额：")
#
# #3.计算余额并输出 ---> money转为int类型 ---int(..)
# print(f"取款后您的银行卡的的余额为：{total - int(money)}")

a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
print(f"两数之和为：{a+b}")