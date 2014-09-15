""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""

loops = range(1000)

### Flyweight

class Fly:
    
    a = 1
    b = 2

class FlyObject(object):
    
    a = 1
    b = 2

class FlyStorage:

    counter = -1
    data = None
    Fly = Fly
    
    def __init__(self):
        self.counter = -1
        self.data = {}

    def create_fly(self, *args):
        f = self.Fly(*args)
        self.counter += 1
        i = self.counter
        self.data[i] = tuple(f.__dict__.items())
        return i

    def get_fly(self, i):
        f = self.Fly()
        f.__dict__ = dict(self.data[i])
        return f

class FlyObjectStorage(FlyStorage):

    Fly = FlyObject

###

def create_list_of_fly_objects():
    l = [Fly() for i in loops]
    return l

assert len(create_list_of_fly_objects()) == len(loops)

def create_list_of_fly_flyweights():
    storage = FlyStorage()
    l = [storage.create_fly() for i in loops]
    return l, storage

l, storage = create_list_of_fly_flyweights()
assert len(l) == len(loops)
assert isinstance(storage.get_fly(1), Fly)

filled_fly_storage = storage

def retrieve_list_of_fly_flyweights():
    storage = filled_fly_storage
    l = [storage.get_fly(i) for i in loops]
    return l, storage

def create_list_of_flyobject_objects():
    l = [FlyObject() for i in loops]
    return l

assert len(create_list_of_flyobject_objects()) == len(loops)

def create_list_of_flyobject_flyweights():
    storage = FlyObjectStorage()
    l = [storage.create_fly() for i in loops]
    return l, storage

l, storage = create_list_of_flyobject_flyweights()
assert len(l) == len(loops)
assert isinstance(storage.get_fly(1), FlyObject)

filled_flyobject_storage = storage

def retrieve_list_of_flyobject_flyweights():
    storage = filled_flyobject_storage
    l = [storage.get_fly(i) for i in loops]
    return l, storage

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
    print
    perftools.memory_check_functions(globals())
    
