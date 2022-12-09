# class Human:
#     height = 170
#     satiety = 50
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# nick = Student()
# ann = Worker()
# print(nick.satiety)
# print(ann.satiety)

# ----------------------

# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
# nick = Child()


# ---------------------

# class Wow:
#     def __wow(self):
#         print("Wow")
#
#     def _hello(self):
#         print("Hello")
#
# some_obj = Wow()
# some_obj._hello()
# some_obj._Wow__wow()

# -------------------------
class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)

hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_print()