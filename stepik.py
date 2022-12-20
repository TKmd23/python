x = int(input())
n = x
list = []
while n > 1:
    if x%n == 0:
        list.append(n)

    n -= 1
print(min(list))    