import csv

with open('test.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['user_id', 'user_name', "user_qty"])
    writer.writerow(['2307', 'tkmd', "2"])
    writer.writerow(['1902', 'Marina', "7"])
    writer.writerow(['2011', 'Alice', "12"])
    writer.writerow(['0906', 'Mom', "9"])

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    csv_list = list(reader)
    print(csv_list)
    # for line in reader:
    #     print(line)