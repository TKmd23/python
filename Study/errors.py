print("Hello")
# print(100+"5")
# print(100/0)
# print(int("test"))

# try:
#     num = 100 / "2"
# except ZeroDivisionError:
#     num = 0
# except TypeError:
#     num = 1

# try:
#     num = 100 / 1
# except Exception:
#     num = 10
# else:   # Only if no exception
#     print("Else")
# finally:   # Always
#     print("Finally")
# print(num)

while 1:
    try:
        num = int(input("Enter your number: "))
        a = 100 / num
    except ZeroDivisionError:
        print("You enter 0? try once more!")
    except ValueError:
        print("Must be a number!")
    else:
        print(f"Thank you for your choice, your number is - {num}")
        break
    finally:
        pass

print("next step")