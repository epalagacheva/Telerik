rows=int(input())
foods=[]
for i in range(1,rows+1):
    food=input()
    foods.append(food)
vowels=[]
lenght=[]
for food in foods:
    a=food.count('a')
    o=food.count('o')
    u=food.count('u')
    e=food.count('e')
    i=food.count('i')
    all= a + o + u + e + i
    vowels.append(all)
    #print(vowels)
    long=len(food)
    lenght.append(long)
    #print(lenght)

ratio = [v / l for v, l in zip(vowels, lenght)]
ratio = ["%.2f" % member for member in ratio]


ra_fo = {ratio[i]: foods[i] for i in range(len(ratio))}
ra_vo = {ratio[i]: vowels[i]for i in range(len(ratio))}

fo_vo = {foods[i]: vowels[i] for i in range(len(foods))}

best_ratio = min(ratio) #za da posochi key koito durji dumata s best ratio
proverka= max(ratio)
if best_ratio==proverka:
    how_long= max(lenght)
    longest=max(foods)
    #print(how_long)
    print(f'{longest} {fo_vo[longest]}/{how_long}')
else:
    len_food= len(ra_fo[best_ratio])
    print(f'{ra_fo[best_ratio]} {ra_vo[best_ratio]}/{len_food} ')