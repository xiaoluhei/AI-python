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
# msg = 'It\'s very good'
# print(msg)
#
# msg2 = "It's very good"
# print(msg2)
#
# msg3 ="Hello 的意思是\"你好\""
# print(msg3)
#
# msg4 = 'Hello 的意思是"你好"'
# print(msg4)
#
# print("\t坚持进行python学习！\n\tgogogo!")# \n换行 \t代表缩进

# 字符串拼接
# 字面量会自动拼接
# s1 = "人生苦短" "我用Python" ", OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用Python"
# print("龟叔说: " + msg1 + "," + msg2)
#
# # 案例 -----> str(int数字) ----> 将int类型数据转为字符串
# name = "lulu"
# age = 24
# pro = "人工智能"
# hobby = "Python、AI"
# message = "大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro +"，爱好" + hobby
# print(message)


# 字符串格式化 -----> 方式一 %s 占位符
name = "lulu"
age = 24
pro = "人工智能"
hobby = "Python、AI"
print("大家好，我是%s，今年%s岁，学习的专业是%s，爱好%s" % (name, age, pro, hobby))

# 字符串格式化 -----> 方式二 f{变量名/表达式} ------>推荐方式
name = "lulu"
age = 24
pro = "人工智能"
hobby = "Python、AI"
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}，爱好%{hobby}")