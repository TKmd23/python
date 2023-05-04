def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = [i for i in s if i < elem]
    right = [i for i in s if i > elem]
    center = [i for i in s if i == elem]

    return quick_sort(left) + center + quick_sort(right)