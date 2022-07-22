import inspect
 
class MyClass(object):
 
    # MyClass property
    property1 = [1, 2, 3]
 
    def __init__(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = a
 
    def add(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state + a
        return self.state
 
 
    def subtract(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state - a
        return self.state
 
 
    def multiply(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state * a
        return self.state
 
 
    def divide(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state / a
        return self.state
 
 
    @staticmethod
    def global_method(a, b):
        return a + b
 
 
    @classmethod
    def myclass_method(cls):
        return cls
 
 
# Create our instance
instance = MyClass(100)
 
# Get the list of functions
method_list = inspect.getmembers(MyClass, predicate=inspect.ismethod)
print(method_list)


print('== instance list == ')
method_list1 = inspect.getmembers(instance, predicate=inspect.ismethod)
print(method_list1)


'''
[('myclass_method', <bound method MyClass.myclass_method of <class '__main__.MyClass'>>)]
== instance list == 
[('__init__', <bound method MyClass.__init__ of <__main__.MyClass object at 0x7fa0ec0e6f40>>), ('add', <bound method MyClass.add of <__main__.MyClass object at 0x7fa0ec0e6f40>>), ('divide', <bound method MyClass.divide of <__main__.MyClass object at 0x7fa0ec0e6f40>>), ('multiply', <bound method MyClass.multiply of <__main__.MyClass object at 0x7fa0ec0e6f40>>), ('myclass_method', <bound method MyClass.myclass_method of <class '__main__.MyClass'>>), ('subtract', <bound method MyClass.subtract of <__main__.MyClass object at 0x7fa0ec0e6f40>>)]
[Finished in 54ms]
'''




