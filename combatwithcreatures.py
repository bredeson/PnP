import re
import sys
import time

goblin = 20

gobatk = 2

prisoner = 40

attack = 5

import Creatures

Goblin = Creatures.Goblin()

while Goblin.hp > 0:
	if prisoner < 1:
		print('you have died; you little bitch')
		break
	elif Goblin.hp > 10:
		print('You strike at the goblin dealing',attack,'damage')
		#time.sleep(3)
		Goblin.hp = Goblin.hp-attack
		print('The goblin looks weakened, but still thriving. It has', Goblin.hp, 'health remaining')
		#time.sleep(3)
		prisoner = prisoner-Goblin.attack
		print('The goblin hit you for', Goblin.attack, 'damage; your health is now',prisoner)
		#time.sleep(3)
		continue
	elif Goblin.hp > 0:
		print('You strike at the goblin dealing',attack,'damage')
		#time.sleep(3)
		Goblin.hp = Goblin.hp-attack
		if Goblin.hp > 0:
			print('The goblin is almost dead. It has', Goblin.hp, 'health remaining')
			#time.sleep(3)
			print('The goblin hit you for', Goblin.attack, 'damage; your health is now',prisoner)
			#time.sleep(3)
			prisoner = prisoner-Goblin.attack
		else:
			print('the goblin is dead')
			break
	else:
		break
