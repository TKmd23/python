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
First.test()
Second.test()