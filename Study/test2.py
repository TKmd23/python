# """dicts"""
# x = 5
#
#
# def func():
#     global x
#     x += 1
#     return x
#
#
# print(x)
# print(func())
# print(x)
# --------------------------

l = [1, "2", 3]


# def f(l):
#     return [i * 2 for i in l]
#
#
# print(f(l))

# def f2(l):
#     def tester(x):
#         return x * 2
#
#     return [tester(i) for i in l]
#
#
# print(f2(l))
# ----------------------

# def f2(l):
#     def tester(x):
#         if isinstance(x, int):
#             return x * 2
#
#     return [tester(i) for i in l if tester(i)]
#
#
# print(f2(l))


def f3(l):
    def tester(x):
        return x * 2

    return list(map(tester, l))


print(f3(l))
