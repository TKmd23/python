# class Computer:
#     def calculate(self):
#         print("Calculating...")
#
# class Display:
#     def display(self):
#         print("I display the image on screen...")
#
# class SmartPhone(Display, Computer):
#     pass
#
# iphone = SmartPhone()
# iphone.calculate()
# iphone.display()

# ----------------------

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 128
        self.model = model


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"


class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone(model="Last")
iphone.print_info()
