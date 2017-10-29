import re
import sys
import time
import random

a = ['strike at the', 'stab at the', 'land a heavy blow against the','slice the', 'swing ferociuosly at the', ]
b = ['takes a beating', 'screams in horror', 'yelps in pain', 'shrieks loudly', 'bleeds heavily', 'laughs at your attack', 'grunts heavily']

import Creatures

Goblin = Creatures.Goblin()

def combat(creature):
	prisoner = 40
#	attack = random.randint(1:6)
	while creature.hp > 0:
		if prisoner < 1:
			print('You have died to a',creature.name,'; you little bitch')
			break
#		elif creature.hp > 10:
#			print('You strike at the', creature.name, 'dealing',attack,'damage')
#			#time.sleep(3)
#			creature.hp = creature.hp-attack
#			print('The',creature.name, 'looks weakened, but still thriving. It has', creature.hp, 'health remaining')
#			#time.sleep(3)
#			prisoner = prisoner-creature.attack
#			print('The',creature.name, 'hit you for', creature.attack, 'damage; your health is now',prisoner)
#			#time.sleep(3)
#			continue
		elif creature.hp > 0:
			attack = random.randint(1,6)
			print('You strike at the',creature.name,'dealing',attack,'damage')
			time.sleep(3)
			creature.hp = creature.hp-attack
			if creature.hp > 0:
				print('The',creature.name, 'takes a beating. It has', creature.hp, 'health remaining')
				time.sleep(3)
				prisoner = prisoner-creature.attack
				print('The', creature.name, 'hits you for', creature.attack, 'damage; your health is now',prisoner)
				time.sleep(3)
			else:
				print('The', creature.name, 'is dead')
				break
		else:
			break

combat(Goblin)
