def dict_to_list(dicter: dict):
    lister = []
    for k, v in dicter.items():
        lister.append((k * 2, v)) if type(k) is int else lister.append((k, v))
    return lister


data = {'test': "fast",
        'test1': "slow",
        6: "new"}

print(dict_to_list(data))
