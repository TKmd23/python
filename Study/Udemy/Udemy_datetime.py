from datetime import date, datetime, timedelta
import time

my_date = date(2023, 8, 15)
# my_time = time(15, 45, 12)
my_datetime = datetime(2022, 12, 10, 18, 10, 45)
print(my_datetime.strftime('%d %b %Y %H:%M:%S'))

date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)

print(my_datetime + timedelta(100))
print('-----------------------')
start_time = time.time()
# print(time.ctime(1512151151))
my_range = list(range(1000_000_00))
print(my_range[10000])
# time.sleep(5)
end_time = time.time()
print(end_time - start_time)
