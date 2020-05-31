"""
print("Hello World!")
print(2333)
print(2.333)
print(None)
print(True,False)
print(())
print([])
print({})

name = "张三"
print("你好,{}",format(name))
"""
#这是单行注释
"""
这是多行注释，注释1
注释2
注释3
"""

"""
print("你好"+name)
print("1,"+"1")
print(((3+2)*100-99)/3)
print(10%3)
print(2>1)

name = input("请输入你的姓名：")
print("这是input获取的值：",name)
"""

"""
1、任何数据都可以转换为字符串；
2、整数和小数之间可以互相转换；
3、字符串转换为其他类型，必须要符合【长得像】；
"""
#元组() 取值 下标
# a = ("哈哈","嘻嘻",233,233,233,True,False,None,2.33,1,0)
# print(a)
# print(a[2])
# print(a.index(233))
# print(a.count(233))
# print(a.count(False))

"""
#数组
b = ["哈哈","嘻嘻",233,233,233,True,False,None,2.33,1,0]
print(b)
print(b[0])
b.append("星期天")  #追加数据
b.insert(2,"插入") #插入数据
print(b)
"""
"""
b = [1,0,34,23,15,46]
# b.sort()
print(b)
b.reverse()
print(b)
b.sort(reverse=True)
print(b)

a = ("哈哈","嘻嘻",233,233,233,True,False,None,2.33,1,0)
b = ["哈哈","嘻嘻",233,233,233,True,False,None,2.33,1,0]
c = (a,b)
d = (b,0)
print(d)
d[0].append("哈哈哈")
print(d)
"""

#字典 字典没有顺序 key:value
XX = {"name":"张三","age":19}
print(XX["name"])
print(XX["age"])

XX.pop("name")
print(XX)
XX.update(name="李四")
print(XX)
b = XX.get("name")
print(b)
b = XX["name"]
print(b)
