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
for line in creatures_list:
	split = line.split('\t')
	