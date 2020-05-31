'''
练习1：请通过input获取两个数字，并计算它们的和。
'''
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))
c = a + b
print("这两个数字的和是：",c)

"""
练习2：请实现一个数字数功能。
"""

a = len(input("请输入："))
print("获取值的长度是：",a)


#输出一个爱心代码
print("\n".join([''.join([('ILOVEYOU'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))