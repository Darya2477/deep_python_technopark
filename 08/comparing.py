import timeit
import weakref

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
    N = 10  # здесь значение N
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

