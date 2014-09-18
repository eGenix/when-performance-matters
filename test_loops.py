""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

### Loops with Python operation

op = lambda x: x*2
seq = range(1000)
result = map(op, seq)

def for_loop():
    l = seq[:]
    for i, x in enumerate(seq):
        l[i] = op(x)
    return l

assert for_loop() == result

def map_loop():
    return map(op, seq)

assert map_loop() == result

def list_comprehension_loop():
    return [op(x) for x in seq]

assert list_comprehension_loop() == result

def generator_loop():
    return list(op(x) for x in seq)

assert generator_loop() == result

### Loops with C function operation

import operator
    
op1 = operator.inv
seq1 = range(1000)
result1 = map(op1, seq1)

def for_loop_c_operation():
    l = seq1[:]
    for i, x in enumerate(seq1):
        l[i] = op1(x)
    return l

assert for_loop_c_operation() == result1

def map_loop_c_operation():
    return map(op1, seq1)

assert map_loop_c_operation() == result1

def list_comprehension_loop_c_operation():
    return [op1(x) for x in seq1]

assert list_comprehension_loop_c_operation() == result1

def generator_loop_c_operation():
    return list(op1(x) for x in seq1)

assert generator_loop_c_operation() == result1
    
###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
