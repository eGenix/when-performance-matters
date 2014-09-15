""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Dictionary lookups

int_dict = dict((x, x+1) for x in loops)

def dict_lookup_int_keys():
    d = int_dict
    for i in loops:
        x = d[i]
    return x

assert dict_lookup_int_keys() == 1000

str_dict = dict((str(x+1000), x+1) for x in loops)
str_keys = [str(i+1000) for i in loops]
    
def dict_lookup_str_keys():
    d = str_dict
    for k in str_keys:
        x = d[k]
    return x

assert dict_lookup_str_keys() == 1000
    
interned_str_dict = dict((intern(str(x+2000)), x+1) for x in loops)
interned_str_keys = [intern(str(i+2000)) for i in loops]
    
def dict_lookup_interned_str_keys():
    d = interned_str_dict
    for k in interned_str_keys:
        x = d[k]
    return x

assert dict_lookup_interned_str_keys() == 1000
    
###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
