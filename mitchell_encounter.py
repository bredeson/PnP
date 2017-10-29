#!/usr/bin/env python3

import creatures, random
hp = 30
#def first_combat(player):
first_combat_query=input("You enter a dark room...an interesting smell looms in the air that makes your stomach rumble.\
 A giant oyster lies the in the middle of the room, but who knows how long it has been there?\
 Do you [eat] the oyster or [keep moving]?\n")
if first_combat_query=="eat":
	oyster = random.randint(-5,5)
	hp += oyster
	if oyster > 0:
		print("The oyster was still good! Your hunger is sated. You gain", oyster, 'hp. Your total hp is', hp)
	elif oyster ==0:
		print('The oyster seemed to do very little, but at least nothing bad has happened...yet')
	else:
		print("The oyster was foul, and your stomach lurches. You lose", oyster, 'hp. Your total hp is', hp)
elif first_combat_query=="keep moving":
        print("You continue onward, ignoring the pang of hunger. Better not to risk it.")
       # decision_counter=2
   # else:
    #    print(sass.sample_sass(), '\n')
   # return(decision_counter)
    
