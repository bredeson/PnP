#!/usr/bin/env python3

#================================================
# Define main user charactrer class and methods
#================================================

import random, time
import creatures
import combatResponses
from textFormat import print_s

class Prisoner(object):
	
	def __init__(self, name = 'Unknown', hp = None, _hp = None,level = 1, difficulty = 'medium', attack = 6, intelligence = 2, location = 'Prison', mana = 3):
		self.name = name
		if difficulty.upper() == 'easy'.upper():
			hp = 40
			intelligence = 3
		elif difficulty.upper() == 'medium'.upper():
			hp = 20
			intelligence = 2
		else:
			hp = 10
			intelligence = 1
		self.intelligence = intelligence
		self.level = level
		self.hp = hp
		self._hp = hp
		self.difficulty = difficulty
		self.attack = attack
		self.location = location
		self.mana = mana

# Combat function for creature encounters --- calls combatResponses for sassy comments during battle

	def combat(self,  monster = None):
		while monster.hp > 0:
			if self.hp <= 0:
				print_s('You have died to a ' + monster.name, color = 'red')
				break
			elif monster.hp > 0:
				combat_query=input('[attack], [risky] attack, or [magic]?\n')
				
				if combat_query == 'attack':
					new_user_attack = random.randint(1,self.attack)
					new_mon_attack = random.randint(1,monster.attack)
					print_s(combatResponses.combatResponse_player(self.attack, new_user_attack) + ' ' + 'You deal ' + str(new_user_attack) + ' damage to ' + monster.name, color = 'red')
					time.sleep(3)
					monster.hp -= new_user_attack
					if monster.hp > 0:
						print_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.')
						time.sleep(3)
						self.hp -= new_mon_attack
						print_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. You health is now ' + str(self.hp), color = 'red')
						time.sleep(3)
					else:
						print_s('The ' + monster.name + ' is dead.')
						break


				if combat_query == 'risky':
					chance = random.randint(1,20)
					min_damage = int(0.5*self.attack)
					max_damage = 2*self.attack
					new_user_attack = random.randint(min_damage,max_damage)
					new_mon_attack = random.randint(1,monster.attack)
					if chance > 10:
						print_s(combatResponses.combatResponse_player(self.attack, new_user_attack) + ' '+ 'You deal ' + str(new_user_attack) + ' damage to ' + monster.name, color = 'red')
						time.sleep(3)
						monster.hp -= new_user_attack
						if monster.hp > 0:
							print_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.')
							time.sleep(3)
							self.hp -= new_mon_attack
							print_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), color = 'red')
							time.sleep(3)
						else:
							print_s('The ' + monster.name + ' is dead.')
							break
					else:
						print_s(combatResponses.missResponse(), color = 'purple')
						time.sleep(3)
						print_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' +  monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), color = 'red')
						self.hp -= new_mon_attack

				if combat_query == 'magic':
					if self.mana > 0:
						new_user_attack = self.attack
						new_mon_attack = random.randint(1,monster.attack)
						print_s(combatResponses.magicResponse() + str(new_user_attack) + ' damage.', color = 'red')
						monster.hp -= new_user_attack
						self.mana -= 1
						print_s('You have ' + str(self.mana) + ' mana left.')
						if monster.hp > 0:
							print_s('The ' + monster.name + ' has ' + str(monster.hp) + ' health remaining.')
							time.sleep(3)
							self.hp -=new_mon_attack
							print_s(combatResponses.combatResponse_monster(monster.attack, new_mon_attack) + ' ' + monster.name + ' does ' + str(new_mon_attack) + ' damage. Your health is now ' + str(self.hp), color = 'red')							
							time.sleep(3)
						else:
							print_s('The ' + monster.name + ' is dead.')
							break
					else:
						print_s('You have no mana left!', color = 'blue')
			else:
				break
# Functions to set self variables

	def setHP(self, new_hp = None):
		self.hp = new_hp

	def setescapeStatus(self, escapeStatus = False):
		self.escapeStatus = escapeStatus

	def setAttack(self, attack_inc = 0):
		self.attack += attack_inc
		print('Your attack damage has increased to ',self.attack,'.\n', sep = '')
