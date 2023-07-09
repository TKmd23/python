import sys

print(sys.argv)

if len(sys.argv) < 3:
    raise IOError("You must enter login and pass")

user_name = sys.argv[1]
user_pass = sys.argv[2]

