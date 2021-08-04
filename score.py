'''
 任务：
 统计，10课程成绩总分，平均分，最高分，最低分。
'''
start = 1
s = []
while start <= 10:
    print("请输入您的第",start,"课成绩：")
    score = input()
    score = int(score)
    s.append(score)
    start = start + 1
print(s)
a=max(s)
print("您的最高分是",a)
print("您的最低分是",min(s))
print("您的平均分是",a/10)
print("您的总分是",sum(s))


