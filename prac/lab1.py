class Array:
   def __init__(self, list):
       self.list = list
       self.cap = 10
       self.elements = 0

   def __eq__(self, other):
       return (type(other) == Array) and (self.list == other.list) and (self.elements == other.elements)

   def __repr__(self):
       return 'list: {}\n elements: {}'.format(self.list, self.elements)

   def checks_cap(self, fname):
       try:
           f = open(fname, "r")
           count = self.elements
           arr1 = self.list
           newcap = self.cap
           for line in f:
               count += 1
               if count >= newcap:
                   newcap = newcap*2
                   arr1 = arr1 + [None]*(newcap//2)
               idx = count-1
               arr1[idx] = line
           newArr = Array(arr1)
           newArr.size = count
           return newArr
       except IOError:
           raise IOError('file name not found')


def empty_array():
    return Array([None]*10)

def check_cap(fname):
   try:
       f = open(fname, "r")
       arr1 = empty_array()
       count = 0
       for line in f:
           count += 1
           if count >= arr1.cap:
               newcap = arr1.cap*2
               arr1 = Array(arr1.list + [None]*(arr1.cap))
               arr1.cap = newcap
           idx = count-1
           arr1.list[idx] = line
       arr1.elements = count
       return arr1
   except IOError:
       raise IOError('file name not found')

fname = 'ex.txt'
print (check_cap(fname))