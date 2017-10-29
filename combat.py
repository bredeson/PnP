import re
import sys
import time
import random

goblin = 20

magic = 3

gobatk = 2

prisoner = 40

attack = 5
maxdmg = 10

while goblin > 0:
	if prisoner < 1:
		print('you have died; you little bitch')
		break
	elif goblin > 0:
		combat_query=input('[attack], [risky] attack, or [magic]?\n')
		if combat_query == 'attack':
			usratk = random.randint(1,6)
			print('You strike at the goblin dealing',usratk,'damage')
			time.sleep(3)
			goblin = goblin-usratk
			if goblin > 0:
				print('The goblin is almost dead. It has', goblin, 'health remaining')
				time.sleep(3)
				print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
				time.sleep(3)
				prisoner = prisoner-gobatk
			else:
				print('the goblin is dead')
				break
		if combat_query =='risky':
			chance = random.randint(1,20)
			min = 0.5*maxdmg
			max = 2*maxdmg
			usratk = random.randint(min,max)
			if chance > 10:
				print('You hit for', usratk, 'damage')
				goblin = goblin-usratk
				if goblin > 0:
					print('The goblin is almost dead. It has', goblin, 'health remaining')
					print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
					prisoner = prisoner-gobatk
				else:
					print('the gob is dead')
					break
			else:
				print('You missed!')
				print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
				prisoner = prisoner-gobatk
		if combat_query =='magic':
				if magic > 0:
					usratk = 6
					print('You do magic stuff for', usratk,'damage')
					goblin = goblin-usratk
					magic -=1
					print ('You have', magic, 'magicjuice left')
					if goblin > 0:
						print('The goblin is almost dead. It has', goblin, 'health remaining')
						print('The goblin hit you for', gobatk, 'damage; your health is now',prisoner)
						prisoner = prisoner-gobatk
					else:
						print('the gob is dead')
						break
				else:
					print('You have no magic juice left')
	else:
		break

