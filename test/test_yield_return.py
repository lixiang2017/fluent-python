


def test_yield():
    yield 3 
    yield 5 
    yield 8 
    return [0, 6, 4]


print(test_yield())
print(list(test_yield()))

for x in test_yield():
    print(x)

'''
<generator object test_yield at 0x7fe0066cf7b0>
[3, 5, 8]
3
5
8
[Finished in 48ms]
'''
