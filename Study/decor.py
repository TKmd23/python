# def hello():
#     return f"Hello, i am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, i am func 'super'")
#     print(func())
#
#
# super_func(hello)
# def hello():
#     return f"Hello, i am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print("Hello, i am func tester")
#
#
# # var = my_decorator(func_test)
# # var()
# func_test()

def capitalizer(func):
    def wrapper():
        string = func()
        string = string.capitalize()
        string = string.replace(",", '')
        return string

    return wrapper


@capitalizer
def hige():
    ss = input()
    return ss


print(hige())
