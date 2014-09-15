""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

### Function calls

result = 3

def python_function():
    a, b = 1, 2
    f = lambda x,y: x+y
    for i in xrange(1000):
        f(a, b)
    return f(a, b)

assert python_function() == result

import operator

def python_c_function():
    a, b = 1, 2
    f = operator.add
    for i in xrange(1000):
        f(a, b)
    return f(a, b)

assert python_c_function() == result

def python_operators():
    a, b = 1, 2
    for i in xrange(1000):
        a + b
    return a + b

assert python_operators() == result

### Method calls

class Class:
    def add(self, a, b):
        return a + b


def python_method():
    test_instance = Class()
    a, b = 1, 2
    f = test_instance.add
    for i in xrange(1000):
        f(a, b)
    return f(a, b)

assert python_method() == result

def python_method_with_lookup():
    test_instance = Class()
    a, b = 1, 2
    for i in xrange(1000):
        test_instance.add(a, b)
    return test_instance.add(a, b)

assert python_method_with_lookup() == result

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
