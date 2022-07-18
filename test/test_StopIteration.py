


def iterResultList():
    for i in range(30, 40):
        #if i > 36:
        #    raise StopIteration
        if i > 36:
            break 
        yield i  



for x in iterResultList():
    print(x)