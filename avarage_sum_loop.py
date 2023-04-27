#On the first line, you will receive N - the number of the values you must read
#On the next N lines you will receive numbers.
a=int(input())

sum=0
for x in range (1,a+1):
    #x=int(input())
    input_number=float(input())
    sum=sum+input_number
av=sum/a
print(f'{av:.2f}')
