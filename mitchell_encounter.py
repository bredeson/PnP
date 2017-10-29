#!/usr/bin/env python3

import creatures, random
hp = 30
#def first_combat(player):
first_combat_query=input("You enter a dark room. As you walk through, you step in a puddle. Crimson blood drips from your boot. .\
 You see a dead guard torn apart. Do you [search] his body or say a prayer and [keep moving]?\n")
if first_combat_query=="search":
	print("You find a vial filled with a mysterious liquid.\n")
	drink_query=input('The bright blue liquid sloshes around the vial. Do you [drink] it or [leave] it.')
	if drink_query=='drink':
		potion = random.randint(-5,5)
		hp += potion
		if potion > 0:
			print("You feel refreshed and gain", potion, 'hp. Your total hp is', hp)
		elif potion ==0:
			print('The potion seemed to have no effect...')
		else:
			print("Your stomach lurches. You lose", potion, 'hp. Your total hp is', hp)
	else:
		print('You ignore the liquid')
elif first_combat_query=="keep moving":
        print("You continue onward, pushing the thought of death out of your mind.")
       # decision_counter=2
   # else:
    #    print(sass.sample_sass(), '\n')
   # return(decision_counter)
    
