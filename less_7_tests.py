# assert 2+2==5, "wrong assert"
# --------------------------
# """
# >>> assertion
# result
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# -------------------------------
# """
# >>> 2+2
# 5
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# -------------------------------
# def adder(*args, **kwargs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwargs.values():
#         result += _
#     return result
# --------------------------------
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == float or type(_) == bool:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == float or type(_) == bool:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result


