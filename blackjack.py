import random
#Dealer Card
dealer_card=[]
#Player Card
player_card=[]

#Deal Card
#Display Card
#Dealer Card
while len(dealer_card)!=2:
    dealer_card.append(random.randint(1,11))
    if len(dealer_card)==2:
        print("Dealer has X &",dealer_card[1])
# Player Card


while len(player_card)!=2:
    player_card.append(random.randint(1,11))
    if len(player_card)!=2:
        print("i hava",player_card)

#Sum of Dealer Card
if sum(dealer_card)==21:
    print("Dealer has 21 and wins")
elif sum(dealer_card)>21:
    print("Dealer has busted")

while sum(player_card)<21:
    action_taken=str(input("Want to stay or hit"))
#Sum of Player Card
    if action_taken=='hit':
        player_card.append(random.randint(1,11))

        print("you now hava total of"+str(sum(player_card))+ " from these cards ", player_card)
    else:
        print("The dealer has a total of " + str(sum(dealer_card)) + " with ", dealer_card)
        print("You have a total of " + str(sum(player_card)) + " with ", player_card)

        if sum(dealer_card)>sum(player_card):
            print("Dealer wins")
        else:
            print("Win")

            break

    if sum(player_card)>21:
        print("Busted! Dealer wins")
    elif sum(player_card)==21:
        print("i hava blackjack!21 Win")
