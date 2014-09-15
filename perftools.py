""" Performance testing tools.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""
import timeit, sys, types

# Debug level
_debug = 0

### Helpers

def find_functions(module_dict):

    """ Find all functions in the given module_dict.

        Returns a dictionary mapping name to function object.

    """
    return dict((name, obj)
                for name, obj in module_dict.iteritems()
                if type(obj) is types.FunctionType
                if '_' in name
                if not name.startswith('_'))

# Types to ignore when recording objects (default)
DEFAULT_IGNORE_TYPES = (types.FunctionType,
                        types.ModuleType,
                        types.BuiltinFunctionType,
                        types.BuiltinMethodType,
                        types.MemberDescriptorType,
                        types.GetSetDescriptorType,
                        types.GeneratorType,
                        types.UnboundMethodType,
                        types.CodeType,
                        )

# Type to not recurse into (default)
DEFAULT_NO_RECURSE_TYPES = ()

# Types to recurse into using the sequence protocol
DEFAULT_RECURSE_SEQUENCE_TYPES = (list,
                                  tuple)

# Types to recurse into using the .iteritems() protocol
DEFAULT_RECURSE_MAPPING_TYPES = (dict,
                                 types.DictProxyType,
                                 )

def record_all_objects(obj, 
                       ignore_types=DEFAULT_IGNORE_TYPES,
                       no_recurse_types=DEFAULT_NO_RECURSE_TYPES,
                       recurse_sequence_types=DEFAULT_RECURSE_SEQUENCE_TYPES,
                       recurse_mapping_types=DEFAULT_RECURSE_MAPPING_TYPES,
                       ignore_classes=True,
                       memo=None):

    """ Record all objects found in the given object obj.

        Recurses into containers, objects, instances and classes.

        Returns a dictionary mapping id() of the object (it's memory
        location) to the object itself.

    """
    if memo is None:
        memo = {}

    # Record obj
    obj_id = id(obj)
    if obj_id in memo:
        return
    if ignore_types and isinstance(obj, ignore_types):
        return
    if _debug:
        print ('Adding object %r at %x to memo' % (obj, obj_id))
    memo[obj_id] = obj
    if no_recurse_types and isinstance(obj, no_recurse_types):
        return

    # Recurse into containers
    if isinstance(obj, recurse_sequence_types):
        # Sequences
        for x in obj:
            if id(x) not in memo:
                record_all_objects(x, memo=memo)

    elif isinstance(obj, recurse_mapping_types):
        # Mappings
        for name, value in obj.iteritems():
            if id(name) not in memo:
                record_all_objects(name, memo=memo)
            if id(value) not in memo:
                record_all_objects(value, memo=memo)

    else:
        # Generics
        if hasattr(obj, '__dict__'):
            # Instances, classes, new-style classes and objects
            if id(obj.__dict__) not in memo:
                record_all_objects(obj.__dict__, memo=memo)
        if hasattr(obj, '__slots__'):
            # New-style classes and objects with slots
            for attrname in obj.__slots__:
                value = getattr(obj, attrname)
                if id(value) not in memo:
                    record_all_objects(value, memo=memo)
        if not ignore_classes and hasattr(obj, '__class__'):
            # Instances, new-style objects
            if id(obj.__class__) not in memo:
                record_all_objects(obj.__class__, memo=memo)

    return memo
            
### Timings

def time_functions(module_dict):

    """ Time all functions in module_dict.

        Uses timeit to do the timing and writes the results to stdout.

    """
    functions = sorted(find_functions(module_dict).iterkeys())
    for name in functions:
        print ('Timing function %s():' % name)
        timeit.main(args=['-s', 'from __main__ import %s' % name,
                          '%s()' % name])
        print ('')

### Memory usage

def total_memory_size(obj):

    """ Calculates the total memory consumed by the given object obj.

        Returns the size in bytes.

    """
    memo = record_all_objects(obj)
    return sum(sys.getsizeof(x)
               for x in memo.itervalues())

def memory_check_functions(module_dict):

    functions = sorted(find_functions(module_dict).iteritems())
    for name, fct in functions:
        print ('Memory check %s():' % name)
        result = fct()
        memsize = total_memory_size(result)
        print ('Return value: %s ...' % (repr(result)[:60]))
        if memsize < 1024:
            memuse = '%5i bytes' % memsize
        elif memsize < 1048576:
            memuse = '%5.2f KB' % (memsize / 1024.0)
        else:
            memuse = '%5.2f MB' % (memsize / 1048576.0)
        print ('Memory use: %s' % memuse)
        print ('')
