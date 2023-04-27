#{largest}, {second_largest} and {third_largest}
a=int(input())

numbers=[]
largest=-500
larges=-500
larg=-500

if a>=3 and a<=20:
    for i in range(0,a):
        input_number=int(input())
        numbers.append(input_number)
    

for number in numbers:
    largest = max(numbers)

index = numbers.index(largest)
numbers.pop(index)

for i in numbers:
    larges= max(numbers)
    
numbers.remove(larges)

for ii in numbers:
    larg=max(numbers)

print(f'{largest}, {larges} and {larg}')