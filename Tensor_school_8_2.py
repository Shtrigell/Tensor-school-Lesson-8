from Animals import Human


class Student(Human):
    '''
    Класс студент, унаследован от класса Human

    Имеет атрибуты:
    dz - домашнее задание

    Имеет ряд перегруженных методов сравнения, для сравнения экземпляров класса по кол-ву сданнных дз.

    '''

    def __init__(self, pathophagy, avg_age, sound, color,gender,social,
                 height, weight, name, dz):
        super().__init__(self, pathophagy, avg_age, sound, color,gender,social,
                 height, weight, name)
        self.dz = dz

    def __lt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz < other_dz

    def __le__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz <= other_dz

    def __eq__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz == other_dz

    def __ne__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz != other_dz

    def __gt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz > other_dz

    def __ge__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz >= other_d
