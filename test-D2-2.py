#列表的增删改和遍历
scores = [90, 85, 88]

#增
scores.append(92)
scores.insert(0,60)
print("增加后：", scores)

#改
scores[0] = 95
print("修改后：", scores)

#删
scores.remove(88)
last = scores.pop()
print("删除后：", scores,"弹出了：", last)

#长度和判断
print("长度：", len(scores))
print("95在不在：", 95 in scores)

#排序
scores.sort()
print("排序后：", scores)
scores.sort(reverse=True)
print("倒序后：", scores)

#遍历
print("---遍历---")
# for s in scores:
#     print(s)
for i in range(len(scores)):
    print(f"第{i+1}个元素:{scores[i]}")

#实验
aaa = [100, 200]
scores.extend(aaa)
for a in aaa:
    print(a)