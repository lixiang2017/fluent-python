



def test_yield():
    yield 5 
    yield 8  
    # raise IndexError
    yield 50
    yield 80 


for x in test_yield():
    print(x)

'''
5
8
[Finished in 83ms]
'''