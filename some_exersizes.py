
lst = ["apple999", "kiwi999", "strawberry000", "tangerine999"]
lst2 = []
for iter in lst:
    if int(iter[-3:]) == 999:
        (lst2.append(iter[:-3]))
print(lst2)


a = 10
for iter in range(5):
    a = a+5

    print(a)


lst = [[1,2,3], ["land", "sea", "sky"]]
for i in lst[0]:
    print(i, lst[1][i-1])

