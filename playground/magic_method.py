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
        print_step(cls.__name__, sys._getframe().f_code.co_name)
        return object.__new__(cls)

    def __init__(self, filepath='./', filename='magic_method.py'):
        self.file = open(join(filepath, filename), 'r+')
        print_step(self.__class__.__name__, sys._getframe().f_code.co_name)
    
    def __del__(self):
        self.file.close()
        del self.file
        print_step(self.__class__.__name__, sys._getframe().f_code.co_name)


if __name__ == "__main__":
    a = ConstructionAndInitialization()