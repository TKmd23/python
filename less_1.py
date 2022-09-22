# class Student:
#     print('Hi')
#     def __init__(self, height=160):
#         self.height = height
#         print("I am alive!")
#         print(self)
#
# first_student = Student()
# second_student = Student(height=180)
#
# print(first_student.height)
# print(second_student.height)


# class Student():
#     amount_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_students += 1
#
# nick = Student()
# kate = Student(height=180)
# print(nick.amount_students)
# print(Student.amount_students)




# class Student():
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
#
# nick = Student()
# kate = Student()



# class Student():
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()


# x = 10
# class Looker():
#     # x = 15
#     print(x)
#     def func_1(self):
#         # x = 20
#         print(x)
#         def func_2():
#             # x = 30
#             print(x)
#         func_2()
# some_obj = Looker()
# some_obj.func_1()


# ***Methods for classes***
# class Student():
#     amount = 0
#     def __init__(self, height=160, name=None):
#         self.name = name
#         self.height = height
#         Student.amount += 1
#     def grow(self, height=1):
#         self.height += height
#     def __str__(self):
#         return f"I am a student. " \
#                f"My name is {self.name}."
#
# nick = Student()
# print(nick.height)
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# adam = Student(name = "Adam")
# print(adam)



# class Student():
#
#     def __init__(self, name=None):
#         self.name = name
#
#     def __del__(self):
#         print("Go home little monkey!")
#
# adam = Student()


# class Student():
#
#     def __init__(self, name=None, height=160):
#         self.name = name
#         self.height = height
#
#     def __bool__(self):
#         return self.name != None
#
#     def __len__(self):
#         return self.height
#
# nick = Student(name="Adam")
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool(nick))

