# a=input()
foods=[]

while True:
    a=input()
    foods.append(a)
    print(foods)
    if a=="END":
        r=foods.remove("END")
        sort=sorted(foods, key=len)
        print(foods)
        print(sort[-1])
        break
    


    