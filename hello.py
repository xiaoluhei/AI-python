def homework1_1():
    print('从今天开始学python')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')

def homework1_2():
    name = input("请输入您的姓名:")
    password = input("请输入您的密码:")
    sex = input("请输入您的性别:")
    print(f"输入成功！您的姓名为:{name},密码为:{password},性别为:{sex}")

def homework1_3():
    course1_score = int(input("请输入第一门成绩:"))
    course2_score = int(input("请输入第二门成绩:"))
    course3_score = int(input("请输入第三门成绩:"))
    avgscore1 = (course1_score >= 90) * 2 + (60 <= course1_score < 90) * 1
    avgscore2 = (course2_score >= 90) * 2 + (60 <= course2_score < 90) * 1
    avgscore3 = (course3_score >= 90) * 2 + (60 <= course3_score < 90) * 1
    score_all = avgscore1 + avgscore2 + avgscore3
    print(f"您的课程总积分为:{score_all}")

def homework1_4():
    N = int(input("输入N的值:"))
    num = 0
    for i in range(1,N+1):
        num = num + i
    print(f"1+2+...+{N}的值为{num}")

def homework1_5():
    #xiaoming = {'语文': 85, '数学': 96, '英语': 88}
    #xiaohong = {'语文': 85, '数学': 96, '英语': 88}
    #xiaoliang = {'语文': 85, '数学': 96, '英语': 88}
    #name = input("输入你的姓名:")
    #score = name['语文'] + name['数学'] + name['英语'] name是字符串，不是字典，用法错了
    #print(f"你的总分是{score}")
    students = {
        '小明': {'语文': 85, '数学': 96, '英语': 88},
        '小红': {'语文': 72, '数学': 80, '英语': 91},
        '小亮': {'语文': 85, '数学': 96, '英语': 88}
    }
    name = input("请输入你的姓名:")#去掉前后空格
    if name in students:
        sorce_dict = students[name]
        total_score = sorce_dict['语文'] + sorce_dict['数学'] + sorce_dict['英语']
        print(f"{name}的总分是{total_score}")
    else:
        print(f"找不到学生: {name}")

def homework1_6():
    nums1 = int(input("输入一班的人数:"))
    class1 = set()
    for i in range(0,nums1):
        class1.add(input("输入一班学生的姓名:"))
    nums2 = int(input("输入二班的人数:"))
    class2 = set()
    for i in range(0,nums2):
        class2.add(input("输入二班学生的姓名:"))

    same_name = class1 & class2
    class2_name = class2 - class1
    for item in same_name:
        print(item)
    for item in class2_name:
        print(item)

