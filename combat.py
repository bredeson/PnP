import re
import sys
import time

goblin = 20

gobatk = 2

prisoner = 40

attack = 5

while goblin > 0:
	if prisoner < 1:
		print('you have died; you little bitch')
		break
	elif goblin > 10:
		print('You strike at the goblin dealing',attack,'damage')
		time.sleep(3)
		goblin = goblin-attack
		print('The goblin looks weakened, but still thriving. It has', goblin, 'health remaining')
		time.sleep(3)
		prisoner = prisoner-gobatk
		print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
		time.sleep(3)
		continue
	elif goblin > 0:
		print('You strike at the goblin dealing',attack,'damage')
		time.sleep(3)
		goblin = goblin-attack
		if goblin > 0:
			print('The goblin is almost dead. It has', goblin, 'health remaining')
			time.sleep(3)
			print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
			time.sleep(3)
			prisoner = prisoner-gobatk
		else:
			print('the goblin is dead')
			break
	else:
		break

