

class PropertyCache(object):
    """
        这是一个具有缓存属性的装饰器
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if not obj:
            return self
        value = self.func(obj)
        setattr(obj, self.func.__name__, value)
        return value