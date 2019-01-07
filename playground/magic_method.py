from os.path import join
import inspect
import sys

'''
    创建和初始化相关
'''
step_counter = 1

def print_step(cls_name, func_name):
    global step_counter
    print(cls_name, 'step', step_counter, ": ", func_name)
    step_counter += 1


class ConstructionAndInitialization(object):
    
    """
        这个是关于对象的 3 个magic方法，
    """

    def __new__(cls):
        '''
            控制如何实现生成一个新的实例，这是 类 级别的方法
            1. 这个方法返回的是一个对象
            2. 关于__new__的使用场景
                2.1 重载 不可变类型 如 int， str tuple等
        '''
        print_step(cls.__name__, sys._getframe().f_code.co_name)
        return super().__new__(cls)

    def __init__(self, filepath='./', filename='magic_method.py'):
        '''
            控制如何初始化一个已经生成好的实例，这是 对象 级别的方法
        '''
        self.file = open(join(filepath, filename), 'r+')
        print_step(self.__class__.__name__, sys._getframe().f_code.co_name)
    
    def __del__(self):
        '''
            其实这个也不常用，因为并不能保证在它一定运行
        '''
        self.file.close()
        del self.file
        print_step(self.__class__.__name__, sys._getframe().f_code.co_name)


class EmployeeSalary(tuple):

    '''
        python3 不在支持 __cmp__ 方法
    '''

    def __new__(cls, iterable):
        '''
            这里算是__new__的一个场景，因为工资一定是整数，
            我们要在创建对象时保证
        '''
        print(cls.__name__, " ", sys._getframe().f_code.co_name, ', with param:', iterable)
        target_iterable = []
        for item in iterable:
            target_iterable.append(abs(int(item)))
        return super().__new__(cls, target_iterable)

    def __gt__(self, other):
        '''
            我们比较基本工资和奖金的和
        '''
        print(self.__class__.__name__, " ", sys._getframe().f_code.co_name, ', sum(self):', sum(self), ', sum(other):', sum(other))
        return  sum(self) > sum(other)

    def __eq__(self, other):
        print(self.__class__.__name__, " ", sys._getframe().f_code.co_name, ', sum(self):', sum(self), ', sum(other):', sum(other))
        return  sum(self) == sum(other)

    def __lt__(self, other):
        '''
            sorted函数使用的是这个方法
        '''
        print(self.__class__.__name__, " ", sys._getframe().f_code.co_name, ', sum(self):', sum(self), ', sum(other):', sum(other))
        return  sum(self) < sum(other)


if __name__ == "__main__":
    '''
        del 执行的时机
    '''
    a = ConstructionAndInitialization()

    a = EmployeeSalary([-30, 100])
    b = EmployeeSalary([20, 200])

    print('salary > compare:', a > b)
    print('salary == compare:', a == b)
    L = [a, b]
    print('sorted([a, b]): ')
    print('\t ', sorted(L))