# -*- coding: utf-8 -*-
'''
@File    :   descriptor.py
@Time    :   2023/01/29 23:23:51
@Author  :   Yishu Zhou 
'''
# 对象属性的访问控制被描述器协议方法重写。这些方法是
# __get__(),__set__(),__delete__(),有这些方法的对象叫描述器
# 仅有get方法的对象被称为non-data descriptor，其他的是data descriptor
# 优先级为 data ＞ 实例属性 ＞ non-data
# 描述器让对象能够自定义属性的查找、存储、删除的操作


# properties、方法、静态方法、类方法、super（）背后的实现机制就是描述器，描述器是个通用协议

class mydescriptor:
    # self是mydescriptor实例，instance是Person类实例，owner是Person类对象
    def __get__(self, instance, owner):
        print('get value:', instance.v)
        return instance.v

    def __set__(self, instance, value):
        print('set value:', value)
        instance.v = value

    def __delete__(self, instance):
        print('delete')
        del instance.v


class Person:
    age = mydescriptor()

    def __init__(self):
        self.age = 100  # 实例属性


p = Person()
print(p.age)  # get
p.age = 10  # set value,只不过set的不是age属性，而是v
print(p.age)  # get
print(p.__dict__)  # 这里没有age这个属性，而是v
del p.age  # 调用的是描述器里的delete方法
print(p.__dict__)

p2 = Person()
print(p2.age)

print('###########################################################')


class mydescriptor2:
    # 只有get方法时是non-data descriptor，优先级低于实例属性
    def __get__(self, instance, owner):
        print('get value:', instance)


class Person2:
    age = mydescriptor2()

    def __init__(self):
        self.age = 100


q = Person2()
q2 = Person2()
print(q.age)
q.age = 10
print(q2.age)
print(q.age)
print(q.__dict__)  # 会发现上述操作并没有调用描述器
del q.age
print(q.__dict__)
