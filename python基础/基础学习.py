# 流程控制 python else if 缩写为elif

age = 18
if age >= 18:
    print("你成年了")
elif age > 0:
    print("你还没成年")
else:
    print("您还未出生")

# for
print("=======")
for a in range(1, 10):
    print(a)
# 输出1 2 ... 9
print("=======")
for a in range(5):
    print(a)
# 输出0 1 2 3 4
print("=======")
s = "hello world"
for a in s:
    print(a)
# 输出h e l l o   w o r l d
print("=======")
for a in range(1, 10, 3):
    print(a)
# 输出1 4 7
print("=======")
list_1 = ["xiong", "shao", "wei"]
for a in list_1:
    print(a)
# 输出xiong shao wei
