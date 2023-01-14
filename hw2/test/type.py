# type(name,base,dict) 类名、父类名组成的元组，字典,输出一个新的type

# 创建类可以有两种方法，直接创建，type创建
class Test1():
    p = 100  # 类属性

    def __init__(self, a, b):
        self.a = a  # 实例属性
        self.b = b

    def lee():
        pass


print(Test1(1, 2))  # Test1的实例
print(type(Test1(1, 2)))  # 查看该实例是如何创造的（通过Test1）
print(Test1(1, 2).__dict__)  # 实例的命名空间
print(getattr(Test1, "p"))


# 类可以创建实例对象，类本身也是对象
print(hasattr(Test1, "newattr"))  # 查看属性
Test1.newattr = "foo"  # 添加属性
print(hasattr(Test1, "newattr"))
print(Test1.newattr)

print(Test1(1, 2).b)  # 实例对象的b属性
print(Test1(1, 2).__dir__())  # 查看实例的所有属性名和方法，包括继承自object类的


# 用type创建
def lee():
    pass


Test2 = type('Test2', (), {"p": 100, "lee": lee, "newattr": "foo"})
t2 = Test2()
t2.a = 1
t2.b = 2
print(t2)
print(t2.__dir__())
