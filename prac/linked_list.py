import sys


# A Linked List contains a
#first, an int and a
#rest, which is either another Linked list or None
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
        self.length = 0

    def __eq__(self, other):
        return (type(other) == Pair) and (self.first == other.first) and (self.rest == other.rest)

    def __repr__(self):
        return ('first: {} rest: {}').format(self.first, self.rest)

def rests(mult):
    return '.rest'*mult


def get(Pair1, index):
    if index < 0 or index >= Pair1.length:
        raise IndexError('index out of range')
    if Pair1 is None or Pair1.first is None:
        return None
    statement = 'Pair1' + rests(index) + '.first'
    return eval(statement)

def add(Pair1, index, val):
    if index < 0 or index > Pair1.length:
        raise IndexError('index out of range')
    if Pair1 is None or Pair1.first is None:
        return Pair(val, None)
    if index == 0:
        return Pair(val, Pair1)
    statement = 'Pair1' + rests(index) + '= Pair(val, Pair1' + rests(index) + ')'
    exec(statement)
    return Pair1

def remove(Pair1, index):
    if index < 0 or index >= Pair1.length:
        raise IndexError('index out of range')
    if Pair1 is None or Pair1.first is None:
        return None


Pair1 = Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None)))))
Pair1.length = 5
print (add(Pair1, 6, 88))