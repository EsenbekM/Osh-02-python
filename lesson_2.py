class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        if isinstance(number, int) and number > 0:
            self.__number = number
        else:
            raise AttributeError("Ошибка! Неверный аттрибут!")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value > 0:
            self.__number = value
        else:
            raise AttributeError("Ошибка! Неверный аттрибут!")


class Animal:
    def __init__(self, name: str, age: int, address: Address):
        self.__name = name
        self.__address = address
        if not isinstance(address, Address):
            raise AttributeError("Invalid address")
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise AttributeError("Ошибка! Неверный аттрибут!")
        self.__is_born()

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_age(self, value):
        if isinstance(value, int) and value > 0:
            self.__age = value
        else:
            raise AttributeError("Ошибка! Неверный аттрибут!")

    def set_name(self, value):
        self.__name = value

    def get_address(self):
        return self.__address

    def __is_born(self):
        print(f"Родился {self.__name}")

    def info(self):
        return f"Name: {self.__name} Age: {self.__age} city: {self.__address.city} " \
               f"street: {self.__address.street} number: {self.__address.number}"

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int, address: Address, commands: list):
        Animal.__init__(self, name, age, address)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super(Dog, self).info() + f" commands: {self.__commands}"

    def speak(self):
        print(f"{self.get_name()} says:gav gav")


class Cat(Animal):
    def __init__(self, name: str, age: int, address: Address):
        Animal.__init__(self, name, age, address)

    def speak(self):
        print(f"{self.get_name()} says: meow meow")


class Fish(Animal):
    def __init__(self, name: str, age: int, address: Address):
        Animal.__init__(self, name, age, address)


address1 = Address("Bishkek", "Ibraimova", 103)
address2 = Address("Osh", "Chui", 12)

ak_tosh = Dog("Ak tosh", 2, address1, ['sit', 'aport'])
albars = Dog("albars", 1, address2, ['sit'])
bobik = Dog("bobik", 2, address1, ['aport'])

barsik = Cat("Barsik", 3, address2)
snezhok = Cat("snezhok", 3, address1)
busik = Cat("busik", 4, address2)

dorri = Fish("Dorri", 1, address1)

animals = [ak_tosh, barsik, albars, snezhok, busik, bobik, dorri]

for animal in animals:
    animal.speak()
    print(animal.info())


class Cow:
    pass


cow1 = Cow()

# print(f"name: {barsik.get_name()} age: {barsik.get_age()}")

# barsik.set_age(5)
#
# print(barsik.get_name())
#
# print(barsik.get_address().street)
#
# print(address1.city)

# address1.city = "Osh"
# print(address1.city)
