class Cheese:
    
    def __init__(self, kind):
        self.kind = kind 

    def __repr__(self):
        return 'Cheese(%r)' % self.kind 

    def __str__(self):
        return '%r' % self.kind 


import weakref 
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese 

# sorted(stock.keys())
print(sorted(stock.keys()))

del catalog 

# sorted(stock.keys())
print(sorted(stock.keys()))

print('repr cheese: ', cheese)
print('str cheese: ', str(cheese))
del cheese 

# sorted(stock.keys())
print(sorted(stock.keys()))


'''
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
['Parmesan']
repr cheese:  'Parmesan'
str cheese:  'Parmesan'
[]
[Finished in 48ms]
'''


