# def checker(var):
#     if type(var) != str:
#         raise TypeError(f"Sorry, we can't work with {type(var)}, we need class str")
#     else:
#         return var
#
# test = 5.5
# checker(test)
# ------------------------------------------------------
# class BuildingError(Exception):
#     def __str__(self):
#         return f"We have no materials"
#
#
# def check(amount, limit):
#     if amount > limit:
#         return "enough"
#     else:
#         raise BuildingError(amount)
#
#
# materials = 250
# print(check(materials, 300))
# ----------------------------------------------
# import warnings
#
# warnings.warn("Warning? no code here", SyntaxWarning)
# ----------------------------------------------
import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning, module not import", ImportWarning)

