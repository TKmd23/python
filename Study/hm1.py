# list = ["even", 4, "even", 1, "even", 55, "odd", 7]
#
#
# def test(l):
#     if "odd" in l:
#         if l.index("odd") in l:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(test(list))

# def find_sum(n):
#     return sum([i for i in range(n+1) if i % 3 == 0 or i % 5 == 0])
#
#
# print(find_sum(10))

def new_list(*args):
    return [i for i in args if len(i) == 4]


print(new_list("mama", "joe", "ffff"))
