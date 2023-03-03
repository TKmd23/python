from datetime import date, datetime, timedelta
import locale  # Для русского варианта

#
# # class date
# today = date.today()
# print(today)  # 2023-03-01
# print(today.day)  # 1
# print(today.weekday())  # 2 (Week starts from 0 - monday)
# print(today.month)  # 3
# print(today.year)  # 2023
# print(type(today.year))  # int
#
# # class datetime
# now = datetime
# print(now.now())  # 2023-03-01 18:06:06.950052
# print(now.today())  # 2023-03-01 18:06:06.950052
# print(type(now.now()))  # <class 'datetime.datetime'>
# print(now.now().day)  # 1
# print(now.now().weekday())  # 2
# print(now.now().month)  # 3
# print(now.now().year)  # 2023
# print(now.now().hour)  # 18
# print(now.now().minute)  # 6
# print(now.now().second)  # 6 <class 'int'>

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
start = datetime.now()
print(start.strftime("%a"))  # Wed / Cp
print(start.strftime("%A"))  # Wednesday / Среда
print(f"Дата: {start.strftime('%A, %d %b %Y')}")  # Дата: среда, 01 мар 2023
print(f"Время: {start.strftime('%H:%M:%S')}")  # Время: 18:25:17
print(start.strftime('%c'))  # 01.03.2023 18:30:02
print(start.strftime('%x'))  # 01.03.2023
print(start.strftime('%X'))  # 18:30:02

delt = datetime.today()

print((delt + timedelta(days=0, hours=2, minutes=10)).strftime('%X'))