import timeit

class Array:
    def __init__(self, list):
        self.list = list
        self.cap = 10
        self.elem = 0

    def __repr__(self):
        return 'list: {} \ncap: {} \nelem: {}\n'.format(self.list, self.cap, self.elem)

    def __eq__(self, other):
        return (type(other) == Array) and (self.list == other.list)


def add(arr1, idx, val):
    if idx > arr1.cap or idx < 0:
        raise IndexError
    if idx == 0:
        newarr = Array([val] + arr1.list)
        newarr.cap = arr1.cap +1
        newarr.elem = arr1.elem +1
        return newarr
    elif idx == arr1.cap:
        newarr = Array(arr1.list + [val])
        newarr.cap = arr1.cap + 1
        newarr.elem = arr1.elem + 1
        return newarr
    else:
        first = arr1.list[:idx]
        rest = arr1.list[idx:]
        newarr = Array(first + [val] + rest)
        newarr.cap = arr1.cap + 1
        newarr.elem = arr1.elem + 1
        return newarr

def remove(arr1, idx):
    if idx >= arr1.cap or idx < 0:
        raise IndexError
    if idx == 0:
        newarr = Array(arr1.list[1:])
        newarr.cap = arr1.cap -1
        if arr1.list[0]:
            newarr.elem = arr1.elem - 1
        else:
            newarr.elem = arr1.elem
        return newarr
    elif idx == arr1.cap-1:
        newarr = Array(arr1.list[:arr1.cap-1])
        newarr.cap = arr1.cap -1
        if arr1.list[arr1.cap-1]:
            newarr.elem = arr1.elem - 1
        else:
            newarr.elem = arr1.elem
        return newarr
    else:
        first = arr1.list[:idx]
        rest = arr1.list[idx+1:]
        newarr = Array(first + rest)
        newarr.cap = arr1.cap - 1
        if arr1.list[idx]:
            newarr.elem = arr1.elem - 1
        else:
            newarr.elem = arr1.elem
        return newarr

arr1 = Array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1.elem =9
arr1.cap = 9
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (timeit.repeat("for x in range(4): remove(arr1, 5)", "from __main__ import remove, arr1", repeat=1, number=1))
print (timeit.repeat("for x in range(4): lista.pop(5)", "from __main__ import add, lista",repeat=1, number=1))

