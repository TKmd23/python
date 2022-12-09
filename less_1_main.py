import random

class Student():

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def sleep(self):
        print("take some dreams")
        self.gladness += 3

    def chill(self):
        print("Rest time!")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Go to the road...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression........")
            self.alive = False
        elif self.progress > 5:
            print("No exams for you!")
            self.alive = False

    def day_end(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.study()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.chill()
        self.day_end()
        self.is_alive()

adam = Student(name="Adam")
print(type(adam))
# for day in range(365):
#     if adam.alive == False:
#         break
#     adam.live(day)


