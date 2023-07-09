import secrets
import string


chars_for_password = string.ascii_letters + string.digits + string.punctuation
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

print(''.join(secrets.choice(chars_for_password) for i in range(20)))



