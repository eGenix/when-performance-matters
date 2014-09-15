""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

### Loops

op = lambda x: x*2
seq = range(1000)
result = map(op, seq)

def for_loop():
    l = seq[:]
    for i in seq:
        l[i] = op(i)
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
    
###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
