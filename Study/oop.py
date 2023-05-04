# class Human:
#
#
#     def __init__(self):
#         self.health = 100
#         self.weight = 50
#         self.name = "que que"
#
#     def say_hello(self, name=""):
#         if name:
#             return "Hi, " + name
#         else:
#             return "Hello, " + self.name
#
# Nick = Human()
#
#
#
# print(Nick.say_hello())

from classes import Person

First = Person(name="Joy")
Second = Person(name="Alice")
# Second._age = 30
# Second.__weight = 70
# print(Second._age)
# print(Second.__weight)
# print(Second._Person__weight)
# Second.set_weight(101)
# print(Second.get_weight())
print(Second.width)
Second.width = 30
print(Second.width)
First.test()
Second.test()
