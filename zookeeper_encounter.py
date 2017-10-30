#!/usr/bin/env python3

import user, creatures, random, time
from sass import sample_sass
from textFormat import input_s, print_s

def zookeeper_encounter(player):
	zookeeper_query=input_s("As you walk around the courtyard, you notice a menagerie of wild animals trapped in cages. A figure dressed in a ringmaster outfit hears you approach and turns around. As he faces you, you realize it's a bipedal lion! He growls at you and demands to know what you are doing in his zoo. How do you respond? [Say nothing], [run] towards the castle, [tell the truth], [lie], or make a lion [pun]\n", player)
	while str(zookeeper_query) not in ["say nothing", "Say nothing", "run", "tell the truth", "pun", 'lie']:
		zookeeper_query=input_s(sample_sass(), player)
	if zookeeper_query=="say nothing" or zookeeper_query== "Say nothing" or zookeeper_query== "run" or zookeeper_query== "tell the truth":
		monster = creatures.Animals()
		print_s("The lion tells you that you do not belong here. He walks away and unlocks a dark cage...revealing a "+ monster.name + ".")
		print(monster.art())
		player.combat(monster)
		player.attack +=2
		input_s("After killing a " + monster.name + ", you are able to fashion a weapon from its remains. Your attack has increased to " + str(player.attack) + ".", player)
	elif zookeeper_query== "pun":
		print_s("You tell the lion that the wizard is your 'mane' man.")
		time.sleep(5)
		print_s("an awkward 'paws' happens as the lion stares at you....")
		time.sleep(5)
		chance = random.randint(1,20)
		if chance > 10:
			print_s("The lion eventually cracks, letting out a hearty chuckle and lets you pass. As you pass he gives you a potion of lion's strength. As you drink it, you feel your muscles growing.")
			player.attack +=2
			input_s("Your attack has increased to " + str(player.attack) + ".", player)
		else:
			monster = creatures.Animals()
			print_s('The lions stares angrily at you, clearly not appreciating your pun. He walks away and unlocks a dark cage revealing...a '+ monster.name + ".")
			print(monster.art())
			player.combat(monster)
			player.attack +=2
			input_s("After killing a " + monster.name + ", you are able to fashion a weapon from its remains. Your attack has increased to " + str(player.attack) + ".", player)
	elif zookeeper_query == 'lie':
		monster = creatures.Animals()
		print_s("You 'lion' to me? You do not belong here! He walks away and unlocks a dark cage...revealing a " + monster.name + ".")
		print(monster.art())
		player.combat(monster)
		player.attack +=2
		input_s("After killing a " + monster.name + ", you are able to fashion a weapon from its remains. Your attack has increased to " + str(player.attack) + ".", player)
	else:
		print_s('edit me')
		
