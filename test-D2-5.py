#综合练习-迷你成绩管理系统
students = [
    {"name":"张三", "chinese":90, "math":85},
    {"name":"李四", "chinese":78, "math":92},
    {"name":"王五", "chinese":88, "math":76},
]

for s in students:
    total = s['chinese'] + s['math']
    s["total"] = total
    print(f"{s['name']}的总分是{s['total']}")

students.append({"name":"赵六", "chinese":95, "math":88})
zhao = students[ 3 ]
zhao[ "total" ] = zhao[ "chinese" ] + zhao[ "math" ]

print(zhao.get( "english" , "缺考" ))

max_score = 0
max_name = ""
for b in students:
    if b['total'] > max_score:
        max_score = b['total']
        max_name = b['name']
print(f"最高分是{max_score}，是{max_name}")
