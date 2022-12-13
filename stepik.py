class Cat:
    def __init__(self, name):
        self.name = name
        self.cat_fullness = 50
        self.house = None


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    # Человек заезжает в дом так
    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} въехал в дом')


class House:

    def __init__(self, number):
        self.number = number
        self.food = 10
        self.money = 0
        self.cat_food = 0
        self.mud = 0


citizen = Man(name='Петя')
cat = Cat(name="Пушок")
citizen.go_to_the_house(house="House")