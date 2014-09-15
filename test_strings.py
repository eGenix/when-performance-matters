""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

### String concat

l = [str(i) for i in range(1000)]
format_str = ''.join(['%s' for i in range(1000)])
result = ''.join(l)

l1 = [[str(i+j) for i in range(4)]
      for j in range(100)]
short_format_str = ''.join(['%s' for i in range(4)])
result1 = ''.join(l1[-1])

def string_concat():
    s = ''
    for part in l:
        s += part
    return s

assert string_concat() == result

def string_join():
    s = ''.join(l)
    return s

assert string_join() == result

def string_format():
    s = format_str % tuple(l)
    return s

assert string_format() == result

### Short string concat

def short_string_concat():
    for seq in l1:
        s = ''
        for part in seq:
            s += part
    return s

assert short_string_concat() == result1

def short_string_join():
    for seq in l1:
        # To be fair, create a new list from the strings before
        # joining them:
        seq = seq[:]
        s = ''.join(seq)
    return s

assert short_string_join() == result1

def short_string_format():
    for seq in l1:
        s = short_format_str % tuple(seq)
    return s

assert short_string_format() == result1

### String concat using other methods

import cStringIO

def string_cstringio():
    s = cStringIO.StringIO()
    write = s.write
    for part in l:
        write(part)
    return s.getvalue()

assert string_cstringio() == result

import array

def string_array():
    s = array.array('c')
    write = s.fromstring
    for part in l:
        write(part)
    return s.tostring()

assert string_array() == result

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
