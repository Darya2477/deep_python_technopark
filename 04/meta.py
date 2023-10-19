class CustomMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('__'):
                new_attr_name = f'custom_{attr_name}'
                new_attrs[new_attr_name] = attr_value

        attrs.update(new_attrs)

        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        cls.custom_val = None
        super().__init__(name, bases, attrs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.custom_val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


assert CustomClass.custom_x == 50
CustomClass.x  # нет ошибки

inst = CustomClass()
assert inst.custom_x == 50
assert inst.custom_val == 99
assert inst.custom_line() == 100
assert str(inst) == "Custom_by_metaclass"

inst.x  # нет ошибки
inst.val  # ошибка
inst.line() # ошибка
inst.yyy  # ошибка

inst.dynamic = "added later"
assert inst.custom_dynamic == "added later"
inst.dynamic  # ошибка