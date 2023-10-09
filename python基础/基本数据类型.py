# 整数
integer_var = 42

# 浮点数
float_var = 3.14159

# 字符串
string_var = "Hello, World!"

# 布尔值
bool_var = True

# 列表
list_var = [1, 2, 3, 4, 5]

# 元组
tuple_var = (10, 20, 30)

# 集合
set_var = {1, 2, 3, 4, 5}

# 字典
dict_var = {'name': 'Alice', 'age': 30}

# 空值
none_var = None

# 输出各个变量的类型和值
print(f"整数: {integer_var}, 类型: {type(integer_var)}")
print(f"浮点数: {float_var}, 类型: {type(float_var)}")
print(f"字符串: {string_var}, 类型: {type(string_var)}")
print(f"布尔值: {bool_var}, 类型: {type(bool_var)}")
print(f"列表: {list_var}, 类型: {type(list_var)}")
print(f"元组: {tuple_var}, 类型: {type(tuple_var)}")
print(f"集合: {set_var}, 类型: {type(set_var)}")
print(f"字典: {dict_var}, 类型: {type(dict_var)}")
print(f"空值: {none_var}, 类型: {type(none_var)}")
print("====================================")
# 强制转换
aaaa = "10"
bbbb = int(aaaa)
print(type(aaaa))
print(type(bbbb))

# 整除 //
# 求幂 **

# 在python中 两端都是字符串才能相加 print("123"+123) 是错误的
print("123"+str(123))
print("你好"* 3)

# python中可以同时为多个变量赋值 区别于其他语言
a=b=2
print(a,b)
a,b,c=1,2,3
print(a,b,c)

# python中 和或非 分别是 and or not

# and的性能优化 当前面是false的情况下 后面就不再执行
a=10
a>0 and print("大于0")
a<0 and print("小于0")

# or的性能优化 当前面是true的情况下 后面就不再执行
a=10
a>0 or print("不大于0")
a<0 or print("不小于0")

age = 18
name = "Xiong"
print("我的名字是%s,我的年龄是%d" % (name,age))

# 输入 input 默认传入的是str类型
name=input("输入你的名字")
print(name)