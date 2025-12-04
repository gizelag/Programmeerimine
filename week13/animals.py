from abc import ABC, abstractmethod


class Animal(ABC):
    animal_type = None

    def __init__(self, name, age:int, gender, weight):

        if not Animal.is_valid_age(age):
            raise ValueError(f"Looma {name} vanus peab olema 0-100 vahel! Saadud: {age}")

        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @staticmethod
    def is_valid_age(age):
        if not isinstance(age, int):
            return False
        if 100 < age or age < 0:
            return False
        return True

    @classmethod
    def calc_age_in_human_years(cls, age):
        looma_age_dict = {"dog": 7,
                          "cat": 6,
                          "bird": 4,
                          "fish": 2
                          }
        if cls.animal_type in looma_age_dict.keys():
            return age * looma_age_dict[cls.animal_type]

    def eat(self):
        print(f"{self.name} sööb maitsvat toitu")

    def sleep(self):
        print(f"{self.name} magab magusalt")

    def get_human_years(self):
        return self.__class__.calc_age_in_human_years(self.age)

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return (f"\nAnimal name: {self.name}\n"
                f"Age: {self.age} years ({self.get_human_years()} in human years))\n"
                f"Gender: {self.gender}\n"
                f"Weight: {self.weight}kg\n")


class Mammal(Animal):
    def __init__(self, name, age, gender, weight, hair_color):
        super().__init__(name, age, gender, weight)
        self.hair_color = hair_color

    def __repr__(self):
        return super().__repr__() + f"Hair color: {self.hair_color}\n"


class Bird(Animal):
    animal_type = "bird"

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight)
        self.wingspan = wingspan
        self.flying_ability = can_fly

    def __repr__(self):
        tekst = "No"
        if self.flying_ability:
            tekst = "Yes"
        return super().__repr__() + f"Wingspan: {self.wingspan}cm. Can fly:{tekst}\n"


class Fish(Animal):
    animal_type = "fish"

    def __init__(self, name, age, gender, weight, max_depth, water_type):
        super().__init__(name, age, gender, weight)
        self.max_depth = max_depth
        self.water_type = water_type

    def __repr__(self):
        return super().__repr__() + f"Max depth: {self.max_depth}m Water type: {self.water_type}\n"


class Dog(Mammal):
    animal_type = "dog"

    def __init__(self, name, age, gender, weight, hair_color, breed):
        super().__init__(name, age, gender, weight, hair_color)
        self.hair_color = hair_color
        self.breed = breed

    def make_sound(self):
        print(f"\n{self.name} haugub: Auh, AUh, Auh!\n")

    def __repr__(self):
        return super().__repr__() + f"Dog breed: {self.breed}\n"


class Cat(Mammal):
    animal_type = "cat"
    def __init__(self, name, age, gender, weight, hair_color, indoor_cat):
        super().__init__(name, age, gender, weight, hair_color)
        self.hair_color = hair_color
        self.indoor_cat = indoor_cat

    def make_sound(self):
        print (f"{self.name} näugub: Mjäu Mjäu!")

    def __repr__(self):
        tekst = "No"
        if self.indoor_cat:
            tekst = "Yes"
        return super().__repr__() + f"Indoor cat: {tekst}\n"


class Eagle(Bird):

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight, wingspan, can_fly)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} karjub: Kiih Kiih")


class Penguin(Bird):
    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight, wingspan, can_fly)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def make_sound(self):
        print(f"\n{self.name} kvääksub: Kvääk Kvääk\n")


class Shark(Fish):
    def __init__(self, name, age, gender, weight, max_depth, water_type, danger_level):
        super().__init__(name, age, gender, weight, max_depth, water_type)
        self.max_depth = max_depth
        self.water_type = water_type
        if 10 < danger_level or danger_level <=0:
            raise ValueError("Danger level must 0-10!")
        else:
            self.danger_level = danger_level

    def make_sound(self):
        print(f"{self.name} teeb: Mull Mull")#

    def __repr__(self):
        return super().__repr__() + f"Danger level: {self.danger_level}/10\n"