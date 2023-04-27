#yes PRODUCT_VALUE
n=int(input())
evens=[]
odds=[]
e=1
o=1
if n>=4 and n<=50:
    for row in range(1, n+1):
        number=int(input())
        if row%2==0:
            evens.append(number)
            e=e*number
        if row%2!=0:
            odds.append(number)
            o=o*number

# print(odds)
# print(evens)
if e==o:
    print(f'yes {e}')
else:
    print(f'no {o} {e}')

        

