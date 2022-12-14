# lister = [1, 2, 3]
# iterator = iter(lister)
# print(iterator)
# ------------------------------
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# ------------------------------
# for el in iterator:
#     print(el)
# for el in iterator:
#     print(el)
# ------------------------------
class Counter:
    def __init__(self, maxNum):
        self.i = 0
        self.maxNum = maxNum

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.maxNum:
            raise StopIteration
        return self.i

count = Counter(10)
# ----------------------------
# for el in count:
#     print(el)
# ----------------------------
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# # print(iter(count))
# print(next(count))