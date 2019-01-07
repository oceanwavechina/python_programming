

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


class Foo:
    def __init__(self):
        self._property_to_be_cached = 'result'

    @PropertyCache
    def property_to_be_cached(self):
        print('compute')
        return self._property_to_be_cached

test = Foo()

print(test.property_to_be_cached)
print(test.property_to_be_cached)