#!/usr/bin/env python3

import re, sys, time, random
from random import randrange

random_creature = None

# Generates a generic class "Creatures" with three attributes with defaults:
# Name, HP (health), and Attack (as a stat/property - treat as noun).
class Creatures:
    def __init__(self, name = "zebrafish", hp = 5, attack = randrange(0,6)):
        self.name = name
        self.hp = hp
        self.attack = attack
	
# Generating a creatures dictionary from a provided text file - prevents manual coding of \
# individual creatures to make things easier and expansion straightforward.

# Entries in dictionary file must be:
# Tab-delimited
# Value will have two values and an optional third:
	# Name
	# HP
	# Attack (Damage)
	## ALWAYS IN THAT ORDER ##
	

creatures_list = open('sample_creatures_list', 'r')
creature_dict = {}
for line in creatures_list:
	split = line.strip().split('\t')
	creature_dict[split[0]] = split[1]	
for key, value in creature_dict.items():
	creature_dict[key] = value.split(',')

# Random selection of creatures for each call of the class - needs to be acknowledged in backbone.

class Random(Creatures):
	def __init__(self, type=None): 
		if type is not None:
			random_creature = type
		else:
			random_creature = random.choice(list(creature_dict))
		self.name = creature_dict[str(random_creature)][0]
		self.hp = int(creature_dict[str(random_creature)][1])
		self.attack = int(creature_dict[str(random_creature)][2])

# Drew has taken care of the random attack value selection - excellent.