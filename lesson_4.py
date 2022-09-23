import random
from time import sleep


class SuperAbility:
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage} "


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        random_hero: Hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super(Boss, self).__str__() + f"Defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Hero, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0 and self.__super_ability != boss.defence:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coef = random.randint(1, 5)
        boss.health -= self.damage * coef
        print(f"CRITICAL DAMAGE {self.damage * coef}!")


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 11)
        print(f"BOOST POINT {boost_point}!")
        for hero in heroes:
            if hero != self and hero.health > 0 and boss.defence != self.super_ability:
                hero.damage += boost_point


class Medic(Hero):
    def __init__(self, name, health, damage, heal_point):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_point = heal_point

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero != self and hero.health > 0 and boss.defence != self.super_ability:
                hero.health += self.__heal_point

    def __str__(self):
        return super(Medic, self).__str__() + f" heal points: {self.__heal_point}"


class Druid(Hero):
    pass


round_number = 0


def is_game_finish(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!")

    return all_heroes_dead


def print_statistic(boss, heroes: list):
    print(f"------------ ROUND {round_number} ------------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)

    for hero in heroes:
        if hero.health > 0 and hero.super_ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistic(boss, heroes)


def start_game():
    boss = Boss("Sauron", 650, 50)

    warrior = Warrior("Teodor", 270, 10)
    mag = Magic("Gendalf", 280, 20)
    medic_1 = Medic("Aibolit", 200, 10, 20)
    medic_2 = Medic("Kamarovskiy", 250, 15, 10)

    heroes = [warrior, mag, medic_1, medic_2]

    print_statistic(boss, heroes)
    print()

    while not is_game_finish(boss, heroes):
        print()
        sleep(3)
        play_round(boss, heroes)


start_game()
