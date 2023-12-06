import copy


class CustomList(list):
    def __create_custom(self, other):
        custom_list = CustomList(self)
        while len(other) > len(custom_list):
            custom_list.append(0)
        return custom_list

    @staticmethod
    def equate_list_length(first: "CustomList", second: "CustomList"):
        first = copy.copy(first)
        second = copy.copy(second)
        max_len = max(len(first), len(second))

        while len(first) < max_len:
            first.append(0)

        while len(second) < max_len:
            second.append(0)

        return zip(first, second)

    @property
    def custom_list(self):
        """custom_list doc"""
        return self

    @custom_list.deleter
    def custom_list(self):
        del self

    def __add__(self, other):
        self = self.__create_custom(other)
        return [x + y for x, y in CustomList.equate_list_length(self, other)]

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self = self.__create_custom(other)
        return [x - y for x, y in CustomList.equate_list_length(self, other)]

    def __rsub__(self, other):
        other = CustomList(other)
        while len(self) > len(other):
            other.append(0)
        for i, elem in enumerate(self):
            other[i] -= elem
        return other

    def __isub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return (sum(self)) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return f'{super().__str__()}, {sum(self)}'
    

