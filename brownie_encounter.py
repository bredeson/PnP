#!/usr/bin/env python3

import user, creatures, random
from sass import sample_sass
from textFormat import input_s, print_s

def brownie_encounter(player):
	brownie_query=input_s("As you ascend the palatial stairway...an interesting smell looms in the air that makes your stomach rumble. A giant brownie lies to one side, but you have some concerning recent memories of a dodgy oyster. Do you [eat] the brownie or [keep moving]?\n", player)
	while str(brownie_query) not in ["eat", "keep moving"]:
		brownie_query=input_s(sample_sass(), player)
	brownie=random.randrange(1,5)
	if brownie_query=="eat":
		print_s("The brownie was still good! Your hunger is sated. You gain"+ str(brownie)+ 'hp. Your total hp is'+ str(player.hp))
		player.hp+=brownie
				
	elif brownie_query=="keep moving":
		print_s("You continue onward, ignoring the pang of hunger. Better not to risk it.")
