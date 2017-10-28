import re, sys, time

class Creatures:
    def __init__(self, name = "zebrafish", hp = 5, attack = 2):
        self.name = name
        self.hp = hp
        self.attack = attack
        
class Goblin(Creatures):
	def __init__(self, name = "goblin", hp = 20, attack = 5):
		self.name = name
		self.hp = hp
		self.attack = attack
		
creatures_list = open('sample_creatures_list', 'r')
creature_dict = {}
for line in creatures_list:
	split = line.strip().split('\t')
	creature_dict[split[0]] = split[1]	
for key, value in creature_dict.items():
	creature_dict[key] = value.split(',')
	
class PrisonGuard(Creatures):
	def __init__(self, name = creature_dict['PrisonGuard'][0], 
	hp = creature_dict['PrisonGuard'][1], attack = creature_dict['PrisonGuard'][2]):
		self.name = name
		self.hp = hp
		self.attack = attack
	
	