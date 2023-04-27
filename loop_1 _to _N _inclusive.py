#1 to N inclusive, on a single line, separated by a whitespace.

n=int(input())

for x in range (1,n+1):
   if x%3==0 or x%7==0:
        continue
    
   print(x, end=' ')
       

        

        
    