# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have problems {exc}")
#     else:
#         print(f"No problems. Result - {result}")
#
#
# def calculate(expression):
#     return eval(expression)
#
#
# checker(calculate, "2+2")
# ------------------------------------
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result - {result}")
#     return checker
#
#
# def calculate(expression):
#     return eval(expression)

# calc = checker(calculate)
# calc("2+2")
# ------------------------------------
def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except Exception as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result - {result}")
        return checker
    return checker


@checker(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)


calculate("2+2")


