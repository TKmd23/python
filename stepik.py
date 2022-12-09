n = int(input())
count = 0
i = 1
while n >= 0:
    count += 1
    x = i * (i + 1) / 2
    n -= x
    i += 1
print(count-1)
