x= int(input())
mini, maxi = 9,0
while x:
    s = x%10
    if s > maxi:
        maxi = s
    if s < mini:
        mini = s
    x=x//10
print(mini, maxi, sep="\n")