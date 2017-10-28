import re, sys, time, random
from random import randrange

# Generates a generic class "Creatures" with three attributes with defaults:
# Name, HP (health), and Attack (as a stat/property - treat as noun).
class Creatures:
    def __init__(self, name = "zebrafish", hp = 5, attack = randrange(0,6)):
        self.name = name
        self.hp = hp
        self.attack = attack
        
# class Goblin(Creatures):
# 	def __init__(self, name = "goblin", hp = 20, attack = 5):
# 		self.name = name
# 		self.hp = hp
# 		self.attack = attack
		
# Generating a creatures dictionary from a provided text file - prevents manual coding of \
# individual creatures to make things easier and expansion straightforward.

creatures_list = open('sample_creatures_list', 'r')
creature_dict = {}
for line in creatures_list:
	split = line.strip().split('\t')
	creature_dict[split[0]] = split[1]	
for key, value in creature_dict.items():
	creature_dict[key] = value.split(',')

class PrisonGuard_Easy(Creatures):
	def __init__(self, name = creature_dict['PrisonGuard_Easy'][0], 
	hp = int(creature_dict['PrisonGuard_Easy'][1]), attack = randrange(0,4)):
		self.name = name
		self.hp = hp
		self.attack = attack

# Sandbox: 
	
attack_vals = list(range(0,7))
random.shuffle(attack_vals)

HP_counter = int()
HP_counter = prisonguard1.hp

# How can I go about getting a new random number for attack each turn? 