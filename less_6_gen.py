# def raise_to_deg(num, maxd):
#     i = 0
#     for _ in range(maxd):
#         yield num ** i
#         i += 1
#
#
# res = raise_to_deg(8, 50)
# print(res)
#
# for _ in res:
#     print(_)
# print("new execution")
# for _ in res:
#     print(_)
# ------------------------------
# def raise_to_deg(num):
#     i = 0
#     while True:
#         yield num ** i
#         i += 1
#
#
# res = raise_to_deg(2)
# for _ in res:
#     print(_)
# ----------------------------
def raise_to_deg(num):
    i = 0
    while True:
        result = num ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1


res = raise_to_deg(2)
for _ in res:
    print(_)
