# The input consists of exactly 3 lines
# x - interval start (inclusive)
# y - interval end (inclusive)
# t - target sum

x=int(input())
y=int(input())
t=int(input())

for chislo in range(x,y+1):
    d1 = chislo % 10
    d2 = chislo % 100 // 10
    d3 = chislo // 100
    sum_of_one= d1+d2+d3
    if sum_of_one == t:
        print(chislo)