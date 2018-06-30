spam = {"name": "Zophie", "age": 7}
spam.setdefault("color", "black")
if "name" in spam:
    print(True)
if "color" in spam.keys():
    print(True)
if 7 in spam.values():
    print(True)
#get 有两个参数 如果 不存在， 返回备用值
print(str(spam.get("name", 0)))
print(str(spam.get("wtf", 0)))
