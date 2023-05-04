n, m = map(int, input().split())
matrix = [input() for i in range(n)]
test = [[False]*m for i in range(n)]

for i in range(n):
    if "S" not in matrix[i]:
        for j in range(m):
            test[i][j] = True

for j in range(m):
    flag = False
    for i in range(n):
        if matrix[i][j] == "S":
            flag = True
            break
    if not flag:
        for i in range(n):
            test[i][j] = True


count = 0
for i in range(n):
    for y in range(m):
        if test[i][y]:
            count+=1
print(count)
