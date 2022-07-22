
from random import shuffle

arr = list(range(10))
shuffle(arr)

print(f'before sorting, arr is {arr}')

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    print(f'one pass, arr is {arr}')

print(f'after sorting, arr is  {arr}')


'''
before sorting, arr is [3, 0, 1, 9, 7, 2, 5, 4, 6, 8]
pass, arr is [9, 0, 1, 3, 7, 2, 5, 4, 6, 8]
pass, arr is [0, 9, 1, 3, 7, 2, 5, 4, 6, 8]
pass, arr is [0, 1, 9, 3, 7, 2, 5, 4, 6, 8]
pass, arr is [0, 1, 3, 9, 7, 2, 5, 4, 6, 8]
pass, arr is [0, 1, 3, 7, 9, 2, 5, 4, 6, 8]
pass, arr is [0, 1, 2, 3, 7, 9, 5, 4, 6, 8]
pass, arr is [0, 1, 2, 3, 5, 7, 9, 4, 6, 8]
pass, arr is [0, 1, 2, 3, 4, 5, 7, 9, 6, 8]
pass, arr is [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
pass, arr is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
after sorting, arr is  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[Finished in 47ms]
'''

'''
before sorting, arr is [7, 3, 4, 2, 1, 5, 0, 9, 8, 6]
one pass, arr is [9, 3, 4, 2, 1, 5, 0, 7, 8, 6]
one pass, arr is [3, 9, 4, 2, 1, 5, 0, 7, 8, 6]
one pass, arr is [3, 4, 9, 2, 1, 5, 0, 7, 8, 6]
one pass, arr is [2, 3, 4, 9, 1, 5, 0, 7, 8, 6]
one pass, arr is [1, 2, 3, 4, 9, 5, 0, 7, 8, 6]
one pass, arr is [1, 2, 3, 4, 5, 9, 0, 7, 8, 6]
one pass, arr is [0, 1, 2, 3, 4, 5, 9, 7, 8, 6]
one pass, arr is [0, 1, 2, 3, 4, 5, 7, 9, 8, 6]
one pass, arr is [0, 1, 2, 3, 4, 5, 7, 8, 9, 6]
one pass, arr is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
after sorting, arr is  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[Finished in 52ms]
'''


