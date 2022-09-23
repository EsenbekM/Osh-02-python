# Class Mixin
class MusicPlayableMixin:
    @staticmethod
    def play_music(song):
        print(f"Играет музыка {song}...")


class Car(MusicPlayableMixin):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print("I can drive")

    def __str__(self):
        return f"Model: {self.model} Year: {self.year}"


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f"{self.model} can drive using electric engine")

    def __str__(self):
        return super(ElectricCar, self).__str__() + f" Battery: {self.battery}"


class FuelCar(Car):
    __total_fuel = 5000

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    @staticmethod
    def fuel_type():
        return "AI - 95"

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f"{self.model} can drive using fuel engine")

    def __str__(self):
        return super(FuelCar, self).__str__() + f" Fuel bank: {self.fuel_bank} Fuel type: {self.fuel_type()}"

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank

    def __sub__(self, other):
        return self.fuel_bank - other.fuel_bank

    def __mul__(self, other):
        return self.fuel_bank * other.fuel_bank

    def __div__(self, other):
        return self.fuel_bank / other.fuel_bank

    def __gt__(self, other):  # >
        return self.fuel_bank > other.fuel_bank and self.year > other.year

    def __lt__(self, other):  # <
        return self.fuel_bank < other.fuel_bank

    def __ge__(self, other):  # >=
        return self.fuel_bank >= other.fuel_bank

    def __le__(self, other):  # <=
        return self.fuel_bank <= other.fuel_bank

    def __ne__(self, other):  # !=
        return self.fuel_bank != other.fuel_bank

    def __eq__(self, other):  # ==
        return self.fuel_bank == other.fuel_bank


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, battery, fuel_bank):
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_bank)


class SmartPhone(MusicPlayableMixin):
    pass


tesla = ElectricCar("Model X", 2022, 80000)
print(tesla)
# print(FuelCar.get_total_fuel())

volvo = FuelCar("Volvo S90", 2023, 70)
print(volvo)
# print(FuelCar.get_total_fuel())

toyota = HybridCar("Toyota Prius", 2018, 50000, 60)
print(toyota)
# print(FuelCar.get_total_fuel())

print(volvo + toyota)
print(volvo - toyota)

print(volvo > toyota)

# tesla.drive()
# volvo.drive()

# toyota.drive()

# tesla.play_music("Максим - Знаешь ли ты?")

# apple = SmartPhone()
# apple.play_music("Numb")

# toyota.fuel_type()
# FuelCar.fuel_type()

# MRO - Method Resolution Order

# print(HybridCar.__mro__)
# print(HybridCar.mro())
