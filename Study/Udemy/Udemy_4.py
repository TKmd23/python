def filter_list(list_to_filter, type_el):
    def check_el(elem):
        return isinstance(elem, type_el)

    return list(filter(check_el, list_to_filter))


data = [1, 2, 'new', 'test']

print(filter_list(data, str))

print(int.__subclasses__())