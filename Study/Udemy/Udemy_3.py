def filter_list(lister: list, type_el):
    result = []
    for el in lister:
        if type(el) is type_el:
            result.append(el)

    return result


data = [1, "test", 4.4, "new"]

print(filter_list(data, str))