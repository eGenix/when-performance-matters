""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Exceptions

def variable_exists_no_exception():
    rc = 0
    this_variable_does_exist = 1
    for i in loops:
        try:
            this_variable_does_exist
        except NameError:
            rc = -1
        else:
            rc = i
    return rc

assert variable_exists_no_exception() == loops[-1]

def variable_does_not_exist():
    rc = 0
    for i in loops:
        try:
            this_variable_does_not_exist
        except NameError:
            rc = i
    return rc

assert variable_does_not_exist() == loops[-1]

class SomeClass:
    pass

def attribute_does_not_exist_instance():
    obj = SomeClass()
    rc = 0
    for i in loops:
        try:
            obj.this_attribute_does_not_exist
        except AttributeError:
            rc = i
    return rc

assert attribute_does_not_exist_instance() == loops[-1]

def attribute_exists_no_exception_instance():
    obj = SomeClass()
    rc = 0
    obj.this_attribute_does_exist = 1
    for i in loops:
        try:
            obj.this_attribute_does_exist
        except AttributeError:
            rc = -1
        else:
            rc = i
    return rc

assert attribute_exists_no_exception_instance() == loops[-1]

class SomeObject(object):
    pass

def attribute_does_not_exist_object():
    obj = SomeObject()
    rc = 0
    for i in loops:
        try:
            obj.this_attribute_does_not_exist
        except AttributeError:
            rc = i
    return rc

assert attribute_does_not_exist_object() == loops[-1]

def attribute_exists_no_exception_object():
    obj = SomeObject()
    rc = 0
    obj.this_attribute_does_exist = 1
    for i in loops:
        try:
            obj.this_attribute_does_exist
        except AttributeError:
            rc = -1
        else:
            rc = i
    return rc

assert attribute_exists_no_exception_object() == loops[-1]

def attribute_does_not_exist_getattr():
    obj = SomeObject()
    rc = 0
    for i in loops:
        getattr(obj, 'this_attribute_does_not_exist', None)
        rc = i
    return rc

assert attribute_does_not_exist_getattr() == loops[-1]

def attribute_exists_getattr():
    obj = SomeObject()
    rc = 0
    obj.this_attribute_does_exist = 1
    for i in loops:
        getattr(obj, 'this_attribute_does_exist', None)
        rc = i
    return rc

assert attribute_does_not_exist_getattr() == loops[-1]

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
