#!/usr/bin/env python3

import user, creatures, random
from sass import sample_sass
from textFormat import input_s, print_s

def oyster_encounter(player):
	oyster_query=input_s("As you enter the sewers...an interesting smell looms in the air that makes your stomach rumble. A giant oyster lies the on the side, but who knows how long it has been there? Do you [eat] the oyster or [keep moving]?\n\n", player)
	while str(oyster_query) not in ["eat", "keep moving"]:
		oyster_query=input_s(sample_sass(), player)

	if oyster_query=="eat":
		oyster = random.randint(-5,5)
		
		player.hp += oyster
		
		if oyster > 0:
			print_s("\nThe oyster was still good! Your hunger is sated. You gain "+ str(oyster)+ ' hp. Your total hp is'+ str(player.hp))
		elif oyster ==0:
			print_s('\nThe oyster seemed to do very little, but at least nothing bad has happened...yet')
		else:
			print_s("\nThe oyster was foul, and your stomach lurches. You lose "+ str(oyster)+ ' hp. Your total hp is '+ str(player.hp))
	
	elif oyster_query=="keep moving":
        	print_s("\nYou continue onward, ignoring the pang of hunger. Better not to risk it.")