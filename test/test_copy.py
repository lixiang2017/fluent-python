'''
shallow copy
A copy of an object which shares references to all the objects that are attributes of the original object. Contrast with deep copy. Also see aliasing.
'''


from copy import copy 
a = [-10, 4, 5, 324398345793470]
b = copy(a)

print(f'list compare {a is b}')

print('item compare')
for i in range(len(a)):
    print(a[i] is b[i])


print('another integer')
c = 324398345793470
print(a[3] is c)


import sys 
print(sys.version_info)


'''
list compare False
item compare
True
True
True
True
another integer
True
sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
[Finished in 51ms]


➜  test git:(master) ✗ python3.9 test_copy.py
list compare False
item compare
True
True
True
True
another integer
True
sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
➜  test git:(master) ✗ python3.8 test_copy.py
list compare False
item compare
True
True
True
True
another integer
True
sys.version_info(major=3, minor=8, micro=6, releaselevel='final', serial=0)


# IPython中没有进行优化，结果不一样
ipython3
Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [17]: from copy import copy
    ...: a = [-10, 4, 5, 324398345793470]
    ...: b = copy(a)
    ...:
    ...: print(f'list compare {a is b}')
    ...:
    ...: print('item compare')
    ...: for i in range(len(a)):
    ...:     print(a[i] is b[i])
    ...:
    ...:
    ...: print('another integer')
    ...: c = 324398345793470
    ...: print(a[3] is c)
    ...:
    ...:
    ...: import sys
    ...: print(sys.version_info)
    ...:
list compare False
item compare
True
True
True
True
another integer
False
sys.version_info(major=3, minor=8, micro=6, releaselevel='final', serial=0)
'''