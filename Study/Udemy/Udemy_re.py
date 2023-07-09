import re

# my_string = "My name is tkmd trnd."

# res = re.search(r'tkmd', my_string)
# res = re.search(r't..d$', my_string)
# res = re.search(r'^t..d', my_string)
# res = re.search(r't..d', my_string)
# res = re.search(r't..d\.$', my_string)
# print(res.span())
# print(res.start())
# print(res.end())
#
# my_pattern = re.compile(r't..d\.$')
# print(my_pattern.search(my_string))
#
# my_pattern = re.compile(r'^My.*d\.$')
# print(my_pattern.match(my_string))


# email_ch = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
# email_ch_pattern = re.compile(email_ch)
# print(email_ch_pattern.fullmatch('kkotolup@gmail.com'))
# print(email_ch_pattern.fullmatch('kkotolupgmail.com'))
# print(email_ch_pattern.fullmatch('kkotolup@gmailcom'))
# print(email_ch_pattern.fullmatch('@gmail.com'))
# print(email_ch_pattern.fullmatch('kkotolup@'))

def check_email(email):
    email_ch = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_ch_pattern = re.compile(email_ch)
    validation = "Valid" if email_ch_pattern.fullmatch(email) else "Invalid"
    return (email, validation)


def check_pass(password):
    pass_ch = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-+])[0-9a-zA-Z!@#$%^&*()-+]{8}$"
    pass_ch_pattern = re.compile(pass_ch)
    validation = "Valid" if pass_ch_pattern.fullmatch(password) else "Invalid"
    return (password, validation)

pass_to_check = 'jl9&23cx'

print(check_pass(pass_to_check))