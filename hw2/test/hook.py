class HookStudy:
    def __init__(self):
        self.make_rice  = None
    def register_rice_hook(self,rice):
        self.make_rice=rice 
    def dinner(self):
        if self.make_rice is None:
            print("no rice")
        else:
            make_rice()
            print('has rice')

def make_rice():
    print('Done!')
#hook函数通过一定关系将两个函数产生关联，要执行make_rice(),
#首先要注册，否则执行一个空的操作


if __name__ == '__main__':
    hk =HookStudy()
    hk.dinner() #直接执行
    hk.register_rice_hook(make_rice) #把要实现的具体细节挂接到钩子函数上
    hk.dinner() #执行流程