# print(type("hello"))
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(False))
# print(type(None))
#
# num = 5
# print(type(num))
#
# # 通过isinstance(num,int)，
# print(isinstance(num,int))

# 字符串
# 定义字符串的三种方式
s1 = "hello" #双引号定义
s2 = 'Python' #单引号定义
s3 = """
Hello:
    坚持进行python学习！
    gogogo!
"""
#三引号定义（多行字符串）
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 定义字符串 ----> It's very good
# 转义字符 \' \" \n \t
msg = 'It\'s very good'
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 ="Hello 的意思是\"你好\""
print(msg3)

msg4 = 'Hello 的意思是"你好"'
print(msg4)

print("\t坚持进行python学习！\n\tgogogo!")# \n换行 \t代表缩进
