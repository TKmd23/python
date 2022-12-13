import random

class animal():

    def __init__(self, name):
        self.name = name
        self.gladness = 10#random.randint(40, 60)
        self.house_live = 100
        self.eate = 15#random.randint(20, 30)
        self.drinck = 50#random.randint(7, 22)

        self.alive = True

    def Walk(self):
        print("Time to go for e wolk!")
        self.house_live -= random.randint(1, 5)
        self.gladness += random.randint(2, 5)
        self.eate -= 5#random.randint(2, 4)
        self.drinck -= 4#random.randint(2, 6)

    def sleep(self):
        print("take some dreams")
        self.gladness += 2#random.randint(2, 8)
        self.eate -= 2#random.randint(0, 3)
        self.house_live += 1
        self.drinck -= 2#random.randint(1, 3)

    def chill(self):
        print("Rest time!")
        self.gladness += 2#random.randint(3, 10)
        self.eate += 2#random.randint(0, 3),
        self.house_live += 2#random.randint(0, 3)
        self.drinck += 2#random.randint(0, 4)

    def eating(self):
        print("Now you are eating")
        self.gladness += random.randint(1, 6)
        self.eate += random.randint(4, 11)
        self.house_live += 1
        self.drinck += random.randint(2, 5)

    def drin(self):
        self.gladness += random.randint(1, 3)
        self.eate += random.randint(0, 3)
        self.house_live += 1
        self.drinck += random.randint(11, 21)

    def bed_outsite_raine(self):
        self.gladness -= random.randint(10, 20)
        self.house_live += random.randint(1, 3)
    print("Its tha rain and you sit at home.")

    def is_alive(self):
        if self.house_live <= -1:
            print("You hawe not a house, (_Game Over!_) ")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression........")
            self.alive = False
        elif self.eate <= 0:
            print("You are die! :(")
            self.alive = False
        elif self.drinck <= 0:
            print("You die because you want drenck!")
            self.alive = False

    def day_end(self):
        print(f"Gladness = {round(self.gladness)}")
        print(f"Life = {round(self.house_live, 2)}")
        print(f"Eate = {round(self.eate, 2)}")
        print(f"Water = {round(self.drinck, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 6)
        if live_cube == 1:
            self.Walk()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.chill()
        elif live_cube == 4:
            self.eating()
        elif live_cube == 5:
            self.drin()
        elif live_cube == 6:
            self.bed()
        self.day_end()
        self.is_alive()

adam = animal(name="Tom")

for day in range(366):
    if adam.alive == False:
        break
    adam.live(day)
