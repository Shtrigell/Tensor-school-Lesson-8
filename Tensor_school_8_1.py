class Animals:
    """ Класс животных

    Имеет атрибуты:
    pathophagy - вид пищи
    avg_age - средний срок жизни
    sound - издаваемый звук
    color - цвет

    """

    def __init__(self, pathophagy, avg_age, sound, color):
        self.pathophagy = pathophagy
        self.avg_age = avg_age
        self.sound = sound
        self.color = color


class Mammals(Animals):
    """ Класс млекопитающих, унаследован от класса Animals

    Имеет атрибуты:
    gender - половая принадлежность 
    social - социльное ли животное

    """

    def __init__(self, pathophagy, avg_age, sound, color,gender,social):
        super().__init__(pathophagy, avg_age, sound, color)
        self.gender = gender
        self.social = social


class Human(Mammals):
    """ Класс человек, унаследован от класса Mammals

    Имеет атрибуты:
    name - имя
    height - рост
    weight - вес

    Имеет методы:
    hello - выводит сообщение с именем человека

    """

    def __init__(self, pathophagy, avg_age, sound, color,gender,social,
                 height, weight, name):
        super().__init__(pathophagy, avg_age, sound, color,gender,social)
        self.height = height
        self.weight = weight
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")


class Cat(Mammals):
    """ Класс кошка, унаследован от класса Mammals

    Имеет атрибуты:
    breed - порода
    dexterity - ловкость

    """

    def __init__(self, pathophagy, avg_age, sound, color, gender, social,breed, dexterity):
        super().__init__(pathophagy, avg_age, sound, color, gender, social)
        self.breed = breed
        self.dexterity = dexterity

    def make_sound(self):
        print(f'{self.sound}')

class Dog(Mammals):

    """ Класс собака, унаследован от класса Mammals

    Имеет атрибуты:
    breed - порода
    devotion - преданность

    """

    def __init__(self, pathophagy, avg_age, sound, color, gender, social,breed,devotion):
        super().__init__(pathophagy, avg_age, sound, color, gender, social)
        self.breed = breed
        self.devotion = devotion

    def make_sound(self):
        print(f'{self.sound}')




