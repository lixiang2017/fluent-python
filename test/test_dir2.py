

class C:
    def __init__(self):
        pass 

    def a(self):
        pass 

    def b(self):
        pass 



'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']
[Finished in 72ms]


In [30]: ??dir
Docstring:
dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class's attributes, and
    recursively the attributes of its class's base classes.
Type:      builtin_function_or_method
'''


class D:
    def __init__(self, xx=879):
        self.x = xx 
        self.y = 435
        self.z = 234

    def a(self):
        pass 

    def b(self):
        pass 

    def __dir__(self):
        return ['a', 'b']

print(dir(D))

for attr in dir(D):
    print(attr, '\t\t', getattr(D, attr))


print('=======callable==========')
for attr in dir(D):
    if callable(getattr(D, attr)):
        print(attr, '\t\t', getattr(D, attr))


'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']
__class__        <class 'type'>
__delattr__          <slot wrapper '__delattr__' of 'object' objects>
__dict__         {'__module__': '__main__', '__init__': <function D.__init__ at 0x7ff00c1e3160>, 'a': <function D.a at 0x7ff00c1e31f0>, 'b': <function D.b at 0x7ff00c1e3280>, '__dir__': <function D.__dir__ at 0x7ff00c1e3310>, '__dict__': <attribute '__dict__' of 'D' objects>, '__weakref__': <attribute '__weakref__' of 'D' objects>, '__doc__': None}
__dir__          <function D.__dir__ at 0x7ff00c1e3310>
__doc__          None
__eq__       <slot wrapper '__eq__' of 'object' objects>
__format__       <method '__format__' of 'object' objects>
__ge__       <slot wrapper '__ge__' of 'object' objects>
__getattribute__         <slot wrapper '__getattribute__' of 'object' objects>
__gt__       <slot wrapper '__gt__' of 'object' objects>
__hash__         <slot wrapper '__hash__' of 'object' objects>
__init__         <function D.__init__ at 0x7ff00c1e3160>
__init_subclass__        <built-in method __init_subclass__ of type object at 0x7ff00c221bb0>
__le__       <slot wrapper '__le__' of 'object' objects>
__lt__       <slot wrapper '__lt__' of 'object' objects>
__module__       __main__
__ne__       <slot wrapper '__ne__' of 'object' objects>
__new__          <built-in method __new__ of type object at 0x10cd38bc0>
__reduce__       <method '__reduce__' of 'object' objects>
__reduce_ex__        <method '__reduce_ex__' of 'object' objects>
__repr__         <slot wrapper '__repr__' of 'object' objects>
__setattr__          <slot wrapper '__setattr__' of 'object' objects>
__sizeof__       <method '__sizeof__' of 'object' objects>
__str__          <slot wrapper '__str__' of 'object' objects>
__subclasshook__         <built-in method __subclasshook__ of type object at 0x7ff00c221bb0>
__weakref__          <attribute '__weakref__' of 'D' objects>
a        <function D.a at 0x7ff00c1e31f0>
b        <function D.b at 0x7ff00c1e3280>
=======callable==========
__class__        <class 'type'>
__delattr__          <slot wrapper '__delattr__' of 'object' objects>
__dir__          <function D.__dir__ at 0x7ff00c1e3310>
__eq__       <slot wrapper '__eq__' of 'object' objects>
__format__       <method '__format__' of 'object' objects>
__ge__       <slot wrapper '__ge__' of 'object' objects>
__getattribute__         <slot wrapper '__getattribute__' of 'object' objects>
__gt__       <slot wrapper '__gt__' of 'object' objects>
__hash__         <slot wrapper '__hash__' of 'object' objects>
__init__         <function D.__init__ at 0x7ff00c1e3160>
__init_subclass__        <built-in method __init_subclass__ of type object at 0x7ff00c221bb0>
__le__       <slot wrapper '__le__' of 'object' objects>
__lt__       <slot wrapper '__lt__' of 'object' objects>
__ne__       <slot wrapper '__ne__' of 'object' objects>
__new__          <built-in method __new__ of type object at 0x10cd38bc0>
__reduce__       <method '__reduce__' of 'object' objects>
__reduce_ex__        <method '__reduce_ex__' of 'object' objects>
__repr__         <slot wrapper '__repr__' of 'object' objects>
__setattr__          <slot wrapper '__setattr__' of 'object' objects>
__sizeof__       <method '__sizeof__' of 'object' objects>
__str__          <slot wrapper '__str__' of 'object' objects>
__subclasshook__         <built-in method __subclasshook__ of type object at 0x7ff00c221bb0>
a        <function D.a at 0x7ff00c1e31f0>
b        <function D.b at 0x7ff00c1e3280>
[Finished in 45ms]
'''

