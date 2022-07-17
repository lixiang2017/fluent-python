import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)

print(wref)
print(wref())
# wref()

a_set = {2, 3, 4}
print(wref())

print(wref() is None)
print(wref() is None)

'''# output
<weakref at 0x7f9fcffc3cc0; to 'set' at 0x7f9fd13f5120>
{0, 1}
None
True
True
[Finished in 49ms]
'''




'''
import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)

wref
wref()

a_set = {2, 3, 4}
wref()
wref() is None
wref() is None
'''

'''
Python 3.9.13 (v3.9.13:6de2ca5339, May 17 2022, 11:23:25)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import weakref
>>>
>>> a_set = {0, 1}
>>> wref = weakref.ref(a_set)
>>>
>>> wref
<weakref at 0x7fa7b9f57d60; to 'set' at 0x7fa7bb350740>
>>> wref()
{0, 1}
>>>
>>> a_set = {2, 3, 4}
>>> wref()
{0, 1}
>>> wref() is None
False
>>> wref() is None
True
'''



