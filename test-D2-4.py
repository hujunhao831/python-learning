#dict进阶
stu = { "name" : "胡峻豪" , "age" : 26 , "city" : "青岛" }

#get的两种用法
print(stu.get("phone"))
print(stu.get("phone", "没有"))
print(stu.get("name"))

#键值一起遍历
for k, v in stu.items():
    print(f"{k} = {v}")
#`.items()` 把每对键值打包成`(键, 值)` ，循环里一次接住两个变量。

#list套dict
students = [
    {"name":"胡峻豪", "age":25},
    {"name":"张三", "age":30},
    {"name":"李四", "age":28},
]
print(students[0]["age"])
print(students[1]["name"])

#遍历列表里的字典
for s in students:
    print(f"{s['name']}:{s['age']}岁")

#challenge
total_age = 0
for a in students:
    total_age += a['age']
print(f"平均年龄是：{total_age/len(students):.1f}")
