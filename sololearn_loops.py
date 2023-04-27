pass_y=int(input())

total=0
pss=[]
for i in range (4):
    pas_y=int(input())
    pss.append(pas_y)

for x in pss:

    if x <=3:
        ticket=0
    if x>=4:
        ticket=100
    total=total +ticket

print(total)