""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Range

def create_range():
    for i in loops:
        l = range(1000)
    return l

assert create_range() == loops

def create_xrange():
    for i in loops:
        l = xrange(1000)
    return l

assert list(create_xrange()) == loops

def loop_range():
    for i in loops:
        l = range(1000)
        for x in l:
            pass
    return l

assert loop_range() == loops

def loop_xrange():
    for i in loops:
        l = xrange(1000)
        for x in l:
            pass
    return l

assert list(loop_xrange()) == loops

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
    print
    perftools.memory_check_functions(globals())
