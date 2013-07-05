
from functools import update_wrapper

__all__ = [
    'buffered_property',
]

class buffered_property(object):
    '''Buffer the result of a method on the class instance'''
    def __init__(self, getter):
        update_wrapper(self, getter)
        self.getter = getter
        self.propname = '__cache__' + getter.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return getattr(instance, self.propname)
        except AttributeError:
            value = self.getter(instance)
            setattr(instance, self.propname, value)
            return value

    def __set__(self, instance, value):
        if instance is None:
            return self
        setattr(instance, self.propname, value)

    def __delete__(self, instance):
        try:
            delattr(instance, self.propname)
        except AttributeError:
            pass

