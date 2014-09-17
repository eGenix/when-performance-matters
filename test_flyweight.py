""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Fly objects

class Fly:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

class FlyObject(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

class FlySlots(object):
    
    __slots__ = ('a', 'b')

    def __init__(self, a, b):
        self.a = a
        self.b = b

### Fly object storages

class FlyStorage(list):

    counter = -1
    Fly = Fly
    max_storage = len(loops)
    
    def __init__(self, max_storage=None):
        if max_storage is None:
            max_storage = self.max_storage
        list.__init__(self, (None,) * max_storage)
        
    def add_fly(self, *args):
        f = self.Fly(*args)
        self.counter += 1
        i = self.counter
        # generic:
        #self.data[i] = tuple(f.__dict__.items())
        self[i] = (f.a, f.b)
        return i

    def get_fly(self, i):
        f = self.Fly(0, 0)
        # generic:
        #f.__dict__ = dict(self.data[i])
        f.a, f.b = self[i]
        return f

class FlyObjectStorage(FlyStorage):

    Fly = FlyObject

class FlySlotsStorage(FlyStorage):

    Fly = FlySlots

    def add_fly(self, *args):
        f = self.Fly(*args)
        self.counter += 1
        i = self.counter
        # generic:
        #self[i] = tuple(getattr(f, x) for x in f.__slots__)
        self[i] = (f.a, f.b)
        return i

    def get_fly(self, i):
        f = self.Fly(0, 0)
        f.a, f.b = self[i]
        return f

### Minimized Fly objects

class MiniFly(tuple):

    def __new__(cls, *args):
        f = Fly(*args)
        return tuple.__new__(cls, (f.a, f.b))

    def emerge(self):
        return Fly(*self)

class MiniFlyObject(tuple):

    def __new__(cls, *args):
        f = FlyObject(*args)
        return tuple.__new__(cls, (f.a, f.b))

    def emerge(self):
        return FlyObject(*self)

class MiniFlySlots(tuple):

    def __new__(cls, *args):
        f = FlySlots(*args)
        return tuple.__new__(cls, (f.a, f.b))

    def emerge(self):
        return FlySlots(*self)

### Fly objects

def create_list_of_fly_objects():
    l = [Fly(3, 4) for i in loops]
    return l

assert len(create_list_of_fly_objects()) == len(loops)

def create_list_of_fly_flyweights():
    storage = FlyStorage()
    for i in loops:
        storage.add_fly(3, 4)
    return storage

storage = create_list_of_fly_flyweights()
assert len(storage) == len(loops)
assert isinstance(storage.get_fly(1), Fly)

filled_fly_storage = storage

def retrieve_list_of_fly_flyweights():
    storage = filled_fly_storage
    l = [storage.get_fly(i) for i in loops]
    return l

def create_list_of_miniflys():
    l = [MiniFly(3, 4) for i in loops]
    return l

### FlyObject objects

def create_list_of_flyobject_objects():
    l = [FlyObject(3, 4) for i in loops]
    return l

assert len(create_list_of_flyobject_objects()) == len(loops)

def create_list_of_flyobject_flyweights():
    storage = FlyObjectStorage()
    for i in loops:
        storage.add_fly(3, 4)
    return storage

storage = create_list_of_flyobject_flyweights()
assert len(storage) == len(loops)
assert isinstance(storage.get_fly(1), FlyObject)

filled_flyobject_storage = storage

def retrieve_list_of_flyobject_flyweights():
    storage = filled_flyobject_storage
    l = [storage.get_fly(i) for i in loops]
    return l

def create_list_of_miniflyobjects():
    l = [MiniFlyObject(3, 4) for i in loops]
    return l

assert len(create_list_of_miniflyobjects()) == len(loops)

### FlySlots objects

def create_list_of_flyslots_objects():
    l = [FlySlots(3, 4) for i in loops]
    return l

assert len(create_list_of_flyslots_objects()) == len(loops)

def create_list_of_flyslots_flyweights():
    storage = FlySlotsStorage()
    for i in loops:
        storage.add_fly(3, 4)
    return storage

storage = create_list_of_flyslots_flyweights()
assert len(storage) == len(loops)
assert isinstance(storage.get_fly(1), FlySlots)

filled_flyslots_storage = storage

def retrieve_list_of_flyslots_flyweights():
    storage = filled_flyslots_storage
    l = [storage.get_fly(i) for i in loops]
    return l

def create_list_of_miniflyslots():
    l = [MiniFlySlots(3, 4) for i in loops]
    return l

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
    print
    perftools.memory_check_functions(globals())
    
