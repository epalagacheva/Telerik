n = int(input())
numbers=[]
for i in range (1,n+1):
    numbers.append(int(input()))
numbers_sorted = sorted(numbers)
print(f'{numbers_sorted[-1]}, {numbers_sorted[-2]} and {numbers_sorted[-3]}')