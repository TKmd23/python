import random

class Human():
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def repair_car(self):
        pass

    def days_index(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass

class Auto():
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car cannot move")
            return False

    brand_list = {
        "BMW":{"fuel":100, "strength":100, "consumption":6},
        "Lada":{"fuel":50, "strength":40, "consumption":10},
        "Volvo":{"fuel":70, "strength":150, "consumption":8},
        "Ferrari":{"fuel":80, "strength":120, "consumption":14},
    }