import re

# findall: 匹配字符串中所有符合正则的内容
lst1 = re.findall(r"\d+","电话号码:10086,电话号码:10010")
print(lst1)
print("————————————————————")


# finditer: 匹配字符串中所有的内容[返回的是迭代器]
# 从迭代器中获取内容需要使用 .group()
lst2 = re.finditer(r"\d+","电话号码:10086,电话号码:10010")
for i in lst2:
    print(i.group())
print("————————————————————")


# search :找到一个结果就返回，返回match对象，
# 需要使用 .group()
lst3 = re.search(r"\d+","电话号码:10086,电话号码:10010")
print(lst3.group())
print("————————————————————")


# match: 从头开始匹配，相当于正则表达式中加了^
# 匹配不上会报错
lst4 = re.match(r"\d+","10086,电话号码:10010")
print(lst4.group())
print("————————————————————")


# 预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("电话号码:10086,电话号码:10010")
for i in ret:
    print(i.group())
print("————————————————————")

s = """
<div class='jj'><span id='1'>林俊杰</span></div>
<div class='joy'><span id='2'>周杰伦</span></div>
<div class='lay'><span id='3'>张艺兴</span></div>
"""

# (?P<组名>正则): 提取正则选中的内容到组中
obj = re.compile(r"<div class=.*?><span id=.*?>(?P<Star>.*?)</span>",re.S) # re.S 作用：让s能匹配换行符
result = obj.finditer(s)
for i in result:
    print(i.group("Star"))






