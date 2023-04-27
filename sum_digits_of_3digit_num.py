n = input ("Enter a three-digit number:")
n = int (n)
 
d1 = n% 10
d2 = n% 100 // 10
d3 = n // 100
 
print ("Sum of digits of a number:", d1 + d2 + d3)
