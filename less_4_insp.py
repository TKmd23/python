import inspect
import requests
import sys

# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isfunction(requests))
# print(inspect.getmodule(requests.get))
# print(inspect.getmodule(list))

# class Human:
#     def __init__(self, age, height, name="John"):
#         self.name = name
#         self.age = age
#
# sig = inspect.signature(Human)
# for parameter in sig.parameters.values():
#     print(parameter.name, parameter.default)
# ------------------------------------------------
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.argv)
#
# for module_name, module_pass in sys.modules.items():
#     print(module_name, module_pass)
# --------------------------
for _ in dir(__builtins__):
    print(_)
