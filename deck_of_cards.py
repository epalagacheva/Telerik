# deck of cards
x=input()

colors=["spades","clubs","hearts","diamonds"]
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
if x in cards:
    index = cards.index(x)

for i in range(index + 1):
    print(f'{cards[i]} of spades, {cards[i]} of clubs, {cards[i]} of hearts, {cards[i]} of diamonds', end="")
        
    print("")








    
