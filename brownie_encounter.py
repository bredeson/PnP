#!/usr/bin/env python3

import user, creatures, random
from sass import sample_sass
from textFormat import input_s, print_s, input_ss

def brownie_encounter(player):
	brownie_query=input_ss("As you ascend the palatial stairway...an interesting smell looms in the air that makes your stomach rumble. A giant brownie lies to one side, but you have some concerning recent memories of a dodgy oyster. Do you [eat] the brownie or [keep moving]?\n", player)
	brownie=random.randrange(1,5)
	if brownie_query=="eat":
		player.hp+=brownie
		print_s("The brownie was still good! Your hunger is sated. You gain "+ str(brownie)+ ' hp. Your total hp is '+ str(player.hp)+ ".")
				
	elif brownie_query=="keep moving":
		print_s("You continue onward, ignoring the pang of hunger. Better not to risk it.")
