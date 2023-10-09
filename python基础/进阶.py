# len
s = "helloworld"
print(len(s))

# find 返回第一次出现的位置
print(s.find("l"))

# startswith endswitch
print(s.startswith("hello"))
print(s.endswith("dl"))

# count
print(s.count("l"))

# replace 替换
print(s.replace("l", "L"))

# split 分割
s1 = "1#2#3#4#5"
print(s1.split("#"))

# upper lower 大写 小写
print(s.upper())
print(s.lower())

# strip 去空格 只能去两边的空格
s2 = "  hello  world  "
print(s2.strip())

# join
s3 = "!!"
print(s3.join(s))
