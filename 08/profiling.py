import cProfile
from comparing import OrdinaryClass, SlotClass, WeakRefClass, create_objects, change_objects

cProfile.run('create_objects(OrdinaryClass, 10, 20)')
cProfile.run('create_objects(SlotClass, 10, 20)')
cProfile.run('create_objects(WeakRefClass, 10, 20)')

cProfile.run('change_objects(create_objects(OrdinaryClass, 10, 20))')
cProfile.run('change_objects(create_objects(SlotClass, 10, 20))')
cProfile.run('change_objects(create_objects(WeakRefClass, 10, 20))')