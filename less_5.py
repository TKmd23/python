# print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
# -----------------------------------------------------
# try:
#     '''code with possible error'''
# except:
#     '''code executed in case error'''
# --------------------------------------------------------
# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except NameError:
#     print("We have an error")
#
# print("code after capsule")
# --------------------------------------------------------
# try:
#     print("start code")
#     print(10/0)
#     print("no errors")
# except NameError:
#     print("We have an NameError")
# except ZeroDivisionError:
#     print("We have an ZeroDivisionError")
# print("end code")
# -------------------------------------------------
# try:
#     print("start code")
#     print(10/0)
#     print("no errors")
# except (NameError, ZeroDivisionError):
#     print("We have an Error")
#
# print("end code")
# -----------------------------------------------------
# try:
#     print("start code")
#     print(10/0)
#     print("no errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print("end code")
# -----------------------------------------------------
# try:
#     try:
#         print("start code")
#         print(error)
#         print("no errors")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)
# -----------------------------------------------------
# try:
#     print("Hello")
# except:
#     print("We have problems")
# else:
#     print("no problems")
# --------------------------------------------------
# try:
#     print("try code")
#     # print(error)
# except NameError as error:
#     print("except code")
#     print(error)
# else:
#     print("else code")
# finally:
#     print("Finally code")