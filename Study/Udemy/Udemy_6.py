dicter = {'first': "try", 'second': "some", ' third': "do it"}

print({k.upper(): v for k, v in dicter.items()})

lister = ['mother', 'father', 'sister', 'bro']

print([i for i in lister if len(i) > 3])