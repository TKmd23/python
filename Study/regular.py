import re


# string = 'Это просто строка текста. А это вторая строка текста.'
# pattern = 'строка'
# pattern2 = 'Это'
# print(string.find(pattern))
# print(pattern in string)

# search metod
# if re.search(pattern, string):
#     print("matched")
# else:
#     print("NO")
#
# match = re.search(pattern, string)
# print(match)
# print(match.span())
# print(match.start())
# print(match.end())

# match metod
# print(re.match(pattern2, string))

# find_all metod
# print(re.findall(pattern, string))

# split metod
# print(re.split(r"\.", string))

# s = '''Это просто строка текста.
# А это еще одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# А это чтрока с разными символами: "!", "@", "-", "?", "_"
# a\\b\tc
# test string'''

# pattern = r"\w+"  # group +
# pattern = r'[а-я0-9]+'
# pattern = r'\d+'    # can add chines or other numbers
# pattern = r'[\d-]'
# pattern = r'a\\b\tc'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

# s = 'kortes@gmail.com'
# pattern = r'^\w+'   # ^ - start; $ - finish
# print(re.findall(pattern, s, flags=re.IGNORECASE))

def validator(email):
    return bool(re.match(r'^.+@\w+\.[a-z]{2,6}$', email, flags=re.IGNORECASE))


s = 'kortes@gmail.com'
print(validator(s))