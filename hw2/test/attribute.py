# -*- coding: utf-8 -*-
'''
@File    :   attribute.py
@Time    :   2022/12/31 21:29:34
@Author  :   Yishu Zhou 
'''
# Start typing your code from here


class TestGetattribute(object):
    def __init__(self, name):
        self.name = name
        self.age = 18

# 自定义getattribute方法，如果不定义的话就默认调取object类里的方法
    def __getattribute__(self, *args, **kwargs):
        if args[0] == "name":
            return "False"
        elif args[0] == "age":
            print("success!")
            return object.__getattribute__(self, *args, **kwargs)


Test1 = TestGetattribute("zhouyishu")
# 当类中属性被访问时，会自动调用__getattribute__方法
print(Test1.name)
print("------------------")
print(Test1.age)
