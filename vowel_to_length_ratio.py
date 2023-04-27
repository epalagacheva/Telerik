#The vowels are 'aouei'
aa=int(input())
foods=[]
vowel=0
vowels=[]

for word in range(1,aa+1):
    b=input()
    foods.append(b)
    sort=sorted(foods, key=len)
    print(sort)
    print(sort[-1])

long_list=[]
for food in sort:
    a=food.count('a')
    o=food.count('o')
    u=food.count('u')
    e=food.count('e')
    i=food.count('i')
    all= a + o + u + e + i
    vowels.append(all)
    print(vowels)
    if all>vowel:
        vowel=all

for item in sort:
    long_list.append(len(item))

print(long_list)

res = {sort[i]: vowels[i] for i in range(len(sort))}
print("Dictionary is : " + str(res))

res2 = {sort[i]: long_list[i] for i in range (len(sort))}
print("sort food : long e" + str(res2))

ratio = [m/n for m, n in zip(vowels, long_list)]
rations=[]
for r in ratio:
    rations = {ratio[i]: sort[i] for i in range(len(ratio))}
    best_ratio = min(ratio)
print(rations)

print(best_ratio)
# rounded_b_r=round(best_ratio, 2)
# print(rounded_b_r)
print(f'{rations[best_ratio]} {best_ratio}/ {res2[best_ratio]}')





