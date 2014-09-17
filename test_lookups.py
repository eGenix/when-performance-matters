""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Variable lookups

global_a = 'global'

def variable_lookup_global():
    for i in loops:
        x = global_a
    return x

assert variable_lookup_global() == global_a
    
def variable_lookup_local():
    local_a = 'local'
    for i in loops:
        x = local_a
    return x

assert variable_lookup_local() == 'local'

### Localized global variables

def variable_lookup_function_with_locals():
    local_a = global_a
    def f(a, b, c):
        x = a
        y = b
        return y
    for i in loops:
        x = f(1, 2, 3)
    return x

assert variable_lookup_function_with_locals() == 2

def variable_lookup_function_with_global():
    local_a = global_a
    def f(a, b, c):
        x = local_a
        y = local_a
        return y
    for i in loops:
        x = f(1, 2, 3)
    return x

assert variable_lookup_function_with_global() == global_a

def variable_lookup_function_with_kwargs_global():
    def f(a, b, c, local_a=global_a):
        x = local_a
        y = local_a
        return y
    for i in loops:
        x = f(1, 2, 3)
    return x

assert variable_lookup_function_with_kwargs_global() == global_a

def variable_lookup_function_with_localized_global():
    def f(a, b, c):
        local_a = global_a
        x = local_a
        y = local_a
        return y
    for i in loops:
        x = f(1, 2, 3)
    return x

assert variable_lookup_function_with_localized_global() == global_a

### Attribute lookups

class AttributeClass:
    class_attribute = 3
    instance_attribute = None

    def __init__(self):
        self.instance_attribute = 4

attribute_class_instance = AttributeClass()

def attribute_lookup_instance():
    o = attribute_class_instance
    for i in loops:
        x = o.instance_attribute
    return x

assert attribute_lookup_instance() == 4
    
def attribute_lookup_class():
    o = attribute_class_instance
    for i in loops:
        x = o.class_attribute
    return x

assert attribute_lookup_class() == 3

### Attribute lookups on new style classes

class AttributeObject(object): 
    class_attribute = 3
    instance_attribute = None

    def __init__(self):
        self.instance_attribute = 4

attribute_object_instance = AttributeObject()

def attribute_lookup_object_instance():
    o = attribute_object_instance
    for i in loops:
        x = o.instance_attribute
    return x

assert attribute_lookup_object_instance() == 4
    
def attribute_lookup_object_class():
    o = attribute_object_instance
    for i in loops:
        x = o.class_attribute
    return x

assert attribute_lookup_object_class() == 3

### Slot lookups

class SlotClass(object):
    readonly_slot = 3 # read-only
    #readwrite_slot read/write

    __slots__ = ('readonly_slot', 'readwrite_slot')

    def __init__(self):
        self.readwrite_slot = 4

slot_class_instance = SlotClass()

try:
    SlotClass().readonly_slot = 99
except AttributeError:
    pass
else:
    raise AssertionError('slot not read-only')
try:
    SlotClass().readwrite_slot = 99
except TypeError:
    raise AssertionError('slot not read-write')

def slot_lookup_readwrite():
    o = slot_class_instance
    for i in loops:
        x = o.readwrite_slot
    return x

assert slot_lookup_readwrite() == 4
    
def slot_lookup_readonly():
    o = slot_class_instance
    for i in loops:
        x = o.readonly_slot
    return x

assert slot_lookup_readonly() == 3

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
