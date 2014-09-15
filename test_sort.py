""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""
import operator

loops = range(1000)

### Sorting tuples

seq1 = reversed(loops)
seq2 = loops[:]
seq = zip(seq1, seq2)
result = seq[:]

def key_lambda_sort():
    l = seq[:]
    l.sort(key=lambda x: x[1])
    return l
   
assert key_lambda_sort() == result
    
def key_itemgetter_sort():
    l = seq[:]
    l.sort(key=operator.itemgetter(1))
    return l
   
assert key_itemgetter_sort() == result

### Sorting objects

class Data:
    a = 1
    b = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b
obj_seq = [Data(seq[i][0], seq[i][1]) for i in loops]

# Decorate/sort/undecorate pattern:
obj_result = [d for (i, d) in sorted((d.b, d) for d in obj_seq)]

def key_lambda_attribute_sort():
    l = obj_seq[:]
    l.sort(key=lambda x: x.b)
    return l
   
assert key_lambda_attribute_sort() == obj_result
    
def key_attrgetter_attribute_sort():
    l = obj_seq[:]
    l.sort(key=operator.attrgetter('b'))
    return l
   
assert key_attrgetter_attribute_sort() == obj_result

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
