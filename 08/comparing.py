import timeit
import weakref

N = 1000000

class Param:
    def __init__(self, val):
        self.val = val

class OrdinaryClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class SlotClass:
    __slots__ =("param1", "param2")
    def __init__(self, param1, param2):
        self.param1=param1
        self.param2=param2

class WeakRefClass:
    def __init__(self, param1, param2):
        self.param1=weakref.ref(param1)
        self.param2=weakref.ref(param2)

def create_objects(class_type, param1, param2):
    return [class_type(Param(param1), Param(param2)) for _ in range(N)]

def change_objects(objects):
    for i in objects:
        i.param1, i.param2 = i.param2, i.param1

#создание
print("The time is taken to create N objects of OrdinaryClass: ", timeit.timeit(lambda: create_objects(OrdinaryClass, 10, 20), globals=globals()))
print("The time is taken to create N objects of SlotClass: ", timeit.timeit(lambda: create_objects(SlotClass, 10, 20), globals=globals()))
print("The time is taken to create N objects of WeakRefClass: ", timeit.timeit(lambda: create_objects(WeakRefClass, 10, 20), globals=globals()))

#изменение
print("The time is taken to change attributes of N objects of OrdinaryClass: ", timeit.timeit(lambda: change_objects(create_objects(OrdinaryClass, 10, 20)), globals=globals()))
print("The time is taken to change attributes of N objects of SlotClass: ", timeit.timeit(lambda: change_objects(create_objects(SlotClass, 10, 20)), globals=globals()))
print("The time is taken to change attributes of N objects of WeakRefClass: ", timeit.timeit(lambda: change_objects(create_objects(WeakRefClass, 10, 20)), globals=globals()))

#профилирование памяти

@profile
def ordinary_class_create_memory_profile():
    groups = []
    for i in N:
        groups.append(OrdinaryClass(i, i+1))
    return groups

@profile
def slot_class_create_memory_profile():
    groups = []
    for i in N:
        groups.append(SlotClass(i, i+1))
    return groups

@profile
def weakref_class_create_memory_profile():
    groups = []
    for i in N:
        groups.append(WeakRefClass(i, i+1))
    return groups


#создание
print("The time is taken to create N objects of OrdinaryClass: ", timeit.timeit(lambda: ordinary_class_create_memory_profile(), globals=globals()))
print("The time is taken to create N objects of SlotClass: ", timeit.timeit(lambda: slot_class_create_memory_profile(), globals=globals()))
print("The time is taken to create N objects of WeakRefClass: ", timeit.timeit(lambda: weakref_class_create_memory_profile(), globals=globals()))

#изменение


