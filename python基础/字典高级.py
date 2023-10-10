student = {
    "Name": "John Doe",
    "Age": 18,
    "Gender": "Male",
    "School": "Some High School",
    "Grades": {
        "Math": 95,
        "English": 89,
        "History": 78
    }
}

# 访问字典中的key
# 使用中括号的方式访问不存在的key会报错
print(student["Name"])

# print(student.Name) 不能使用
print(student.get("Name"))

print(student.get("Sex"))

# 字典的修改 2种

student["Name"] = "XiongShaoWei"
print(student.get("Name"))
print(student["Name"])

# 字典的添加key
student["Sex"] = 2
print(student["Sex"])
student["Grades"]["Science"] = 92
print(student)

# 字典的删除key
# del   删除指定的key/删除整个字典
del student["Sex"]
print(student)
# del student 删除整个字典
# clear 清空字典 但保留对象 将所有的key都删除 保留结构
# student.clear()
print(student)
print("====================")
# 字典的遍历
# 遍历字典的key
for key in student.keys():
    print(key)
print("====================")
# 遍历字典的value
for value in student.values():
    print(value)
print("====================")
# 遍历字典的key和value
for key,value in student.items():
    print(key,value)
print("====================")
# 遍历字典的项/元素
for item in student.items():
    print(item)