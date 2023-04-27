#Min Max Sum Average
a=int(input())
nums=[]

if a>=1 and a<=1000:
    for n in range(1,a+1):
        b=int(input())
        if b>=-10000 and b<=10000:
            nums.append(int(b))


for nu in nums:
    min1=min(nums)  
print(f'min={min1:.2f}')

for nun in nums:
    max1=max(nums)
print(f'max={max1:.2f}')

sum1=0
for num in nums:
    sum1=round(sum1+num, 2)
print(f'sum={sum1:.2f}')


for numm in nums:
    avg1= sum1/a
print(f'avg={avg1:.2f}')






