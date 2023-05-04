class Person:
    def __init__(self, name="Que Que", age=20):
        self.name = name
        self._age = age
        self.__weight = 100
        self.__width = 40

    def __str__(self):
        # return f'Name: {self.name}'
        return self.__class__.__name__

    def test(self):
        print(f"My name is {self.name}, {self.__width}, {self.__weight}")

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value in range(1, 100):
            self.__weight = value
        else:
            print("Incorrect weight")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value in range(1, 100):
            self.__width = value
        else:
            print("Incorrect weight")


class Little(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company


    def more(self):
        # self._age = 30
        print(self.company)
