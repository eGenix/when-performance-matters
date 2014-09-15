""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

### Sorting

seq1 = reversed(range(1000))
seq2 = range(1000)
seq = zip(seq1, seq2)
result = seq[:]

def key_lambda_sort():
    l = seq[:]
    l.sort(key=lambda x: x[1])
    return l
   
assert key_lambda_sort() == result
    
import operator
    
def key_itemgetter_sort():
    l = seq[:]
    l.sort(key=operator.itemgetter(1))
    return l
   
assert key_itemgetter_sort() == result

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
