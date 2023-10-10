# =========添加=========
# 添加 append
a_list = ["aaa", "bbb", "ccc"]

a_list.append("ddd")

print(a_list)

# 插入 insert
a_list.insert(1, "AAA")
print(a_list)

# extend 继承 底层是逐一添加
b_list = ["eee", "fff", "jjj"]
a_list.extend(b_list)
print(a_list)

# =========添加=========
print("==============")
# =========修改=========
a_list = ["aaa", "bbb", "ccc", "ddd", "eee"]
a_list[1] = "BBB"
print(a_list)
a_list[1] = "bbb"
# =========修改=========
print("==============")
# =========查找=========
# in
if "aaa" in a_list:
    print("存在\"aaa\"")
else:
    print("不存在\"aaa\"")
# not in
if "fff" not in a_list:
    print("a_list不存在\"fff\"")
else:
    print("a_list存在\"fff\"")
# =========查找=========
# =========删除=========
# 删除特定del
del a_list[2]
print(a_list)
# 删除最后一个pop
a_list.pop()
print(a_list)
# 根据元素的值删除remove
a_list.remove("bbb")
print(a_list)
# =========删除=========
