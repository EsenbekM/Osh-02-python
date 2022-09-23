class Transport:
    #  Входящие параметры
    def __init__(self, model, year, color):  # Конструктор
        self.model = model  # self - Ссылка на объект
        self.year = year  # self.year - аттрибуты объекта (поля)
        self.color = color

    def change_color(self, new_color):
        if isinstance(new_color, str):
            self.color = new_color
        else:
            print("Пиши буквами!")

    def show(self):
        print(f"Model: {self.model} Year: {self.year} Color: {self.color}")


class Plane(Transport):  # DRY - Don't Repeat Yourself
    def __init__(self, model, year, color):
        Transport.__init__(self, model, year, color)


class Car(Transport):  # Чертеж
    wheels = 4  # Классовый аттрибут

    def __init__(self, model, year, color):
        super().__init__(model, year, color)

    def drive(self, city):  # Метод
        print(f"Машина {self.model} едет в {city}...")


class Truck(Transport):
    ''' Это класс для грузовиков '''

    def __init__(self, model, year, color, load_capacity):
        super(Truck, self).__init__(model, year, color)
        self.load_capacity = load_capacity

    def load_cargo(self, product, weight):
        if weight > self.load_capacity:
            print(f"Вези на боинг, я не резиновый (я {self.color}) "
                  f"максимальная груоподьемность {self.load_capacity} kg")
        else:
            print(f"{product} ({weight} kg) загружен в грузовик {self.model}")

    def show(self):
        print(f"Model: {self.model} Year: {self.year} Color: {self.color} Load capacity: {self.load_capacity}")


def addition(x, y):
    return x + y


volvo = Car("Volvo s90", 1990, ["Green", "White"])  # объект
tesla = Car("Tesla Model X", 2022, {'color1': "White"})

boing = Plane("Boing", 2020, "White")

man = Truck("Man 3", 2023, "Розовый", 60000)
kamaz = Truck(load_capacity=25000, model="Kamaz", year=2000, color="Orange")

man.load_cargo("Масло", 60001)

boing.show()
tesla.show()
man.show()

print(Truck.__doc__)

# print(f"Model: {volvo.model} Year: {volvo.year} Color: {volvo.color}")
# print(f"Model: {tesla.model} Year: {tesla.year} Color: {tesla.color}")

# print()
volvo.color = "Black"
# tesla.change_color(24)

# print(volvo)
# print(f"Model: {volvo.model} Year: {volvo.year} Color: {volvo.color}")
# print(f"Model: {tesla.model} Year: {tesla.year} Color: {tesla.color}")

# print()
# volvo.drive("Бишкек")
# tesla.drive("Ош")

# volvo.show()

# volvo.change_color("Yellow")

# volvo.show()
# print(volvo.wheels)
Car.wheels = 6

# print(volvo.wheels)
# boing.show()

#
# a = 'efw'
# a.lower()
