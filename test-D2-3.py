#字典基础
stu = {"name":"胡峻豪", "age":25, "city":"青岛"}

#取值
print(stu["name"])
print(stu["age"])

#增
stu["score"] = 99
print("增加后：", stu)

#改
stu["age"] = 26
print("修改后：", stu)

#删
del stu["city"]
print("删除后：", stu)

#键的判断和长度
print("name在不在：", "name" in stu)
print("胡峻豪在不在：", "胡峻豪" in stu)
print("长度：", len(stu))