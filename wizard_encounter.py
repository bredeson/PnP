#!/usr/bin/env python3

#===============================
#Final Wizard Encounter
# By Shasta Webb
# 20 October 2017
# filename = wizard_encounter.py
#===============================

#=====================
#Required modules:
# 1) random
# 2) os
# 3) sass
# 4) user
# 5) textFormat
#====================

import user
import random
import sass
from textFormat import print_s, input_s
import creatures

#================================================
# This is the final encounter of the game!
# In this encounter, the Prisoner meets a spooky
# wizard (Simon) and his band of apprentices (TAs)
# who present a multi-step riddle. There are 
# consequences to intelligence points if the user 
# fails to solve the puzzle.
#===============================================


#===============================================
# Defining a global variable for wizard art
# Defining a dictionary of parts of a puzzle
#==============================================

wizard = creatures.Wizard()

final_puzzle = {
		'Part I':  {
				'Question':'Bluejeans Desks is an anagram for which three mages? List them in alphabetical order!',
				'Answer'  :'deb jessen lukas'
		},
		'Part II': {
				'Question':'Eked Emeriti Mixing is an anagram of which three mages? List their first names, but in alphabetical order according to their last names.',
				'Answer'  :'mike xengie demitri'
		},
		'Part III': {
				'Question':'What is the name of the man who wrote the Wizard\'s and Sorceress\' favorite programming language?',
				'Answer'  :'larry wall'
		}
}

#==================================
# Creating a class Wizard_encounter
#=================================

class Wizard_encounter(object):
	
	def __init__(self, completed = False):
		self.completed = completed

#=================================
# Definining final_puzzle function  
#=================================

	def boss_battle(self, user_answer = None, user = None, completed = False):
		try_counter = user.intelligence
		print_s('\n\nYou cautiously step through the door to the highest room in the highest tower. Your stomach churns a bit from the oyster, brownie, and whiskey you may have consumed. Despite boratk\'s sewer, the jbrownie, the magic wombats, and the eleven stairs you climbed, you\'ve somehow made it to the end. You encounter a wizard named Simon, a sorceress named Sofia (who may or may not look familiar) and their band of apprentices dressed in glittering cloaks patterned with python calligraphy and twinkling perls. The wizard turns to you and asks in an English accent with a hint of San Fransciso vernacular, \'Do you wish you gain our respect and win the game?\' Realizing you have no choice, you accept the challenge!\n\n')
		print(wizard.art())
		input_s('Press [Enter] to proceed.', user)

#====================
# Final Puzzle Part I
#====================	
	
		while try_counter > 0:
			user_answer = input_s('\n' + final_puzzle['Part I']['Question'] + '\n\n', user) 
		
			if user_answer.lower() == final_puzzle['Part I']['Answer']:
				try_counter = user.intelligence
				proceed = input_s('\n{} is correct, but you are not finished yet. Press [enter] to proceed to Part II.\n'.format(final_puzzle['Part I']['Answer']), user, color = 'green')
				break

			elif user_answer.lower() != final_puzzle['Part I']['Answer']:
				try_counter -= 1
				print_s('\n{} is incorrect! You have {} more tries.'.format(user_answer, try_counter, final_puzzle['Part I']['Question']), color = 'red')

				if try_counter == 0:
					print_s('\nYOU ARE A FAILURE!', color = 'red')
					return(self.completed)

#=====================
# Final Puzzle Part II
#=====================

		print_s('You\'ve managed to make it to Part II, and you\'re that much closer to gaining Wizard Simon and Sorceress Sofia\'s respect. Good luck!')

		while try_counter > 0:			
			user_answer = input_s('\n' + final_puzzle['Part II']['Question'] + '\n\n', user)

			if user_answer.lower() == final_puzzle['Part II']['Answer']:
				try_counter = user.intelligence
				proceed = input_s('\n{} is correct! One challenge remains between you and earning the respect of the cloaked crew. Press [enter] to proceed.\n'.format(final_puzzle['Part II']['Answer']), user, color = 'green')
				break

			elif user_answer.lower() != final_puzzle['Part II']['Answer']:
				try_counter -= 1
				print_s('\n{} is incorrect! You have {} more tries.\n'.format(user_answer, try_counter), color = 'red')

				if try_counter == 0:
					print_s('\nYOU ARE A FAILURE!\n', color = 'red')
					return(self.completed)

#======================
# Final Puzzle Part III
#======================

		print_s('Tension is building as you get to the final puzzle of the game! You\'ve earned the respect of the mages, but Wizard Simon and Sorceress Sofia still require a final test! As devout perl disciples, they are reluctant to let any student pass through their course perl free!') 
			
		while try_counter > 0:			
			user_answer = input_s('\n\n' + final_puzzle['Part III']['Question'] + '\n\n', user)

			if user_answer.lower() == final_puzzle['Part III']['Answer']:
				try_counter = user.intelligence
				proceed = input_s('\n{} is correct! Against all odds, you\'ve earned the respect of the Wizard, Sorceress, and the band of mages. In your state of celebration, it suddenly occurs to you that you still do not know why you woke up in a prison. You recall your day, somewhat hazily, but remain unsure of the crimes you committed. You meekly ask the Wizard, \"Why did I end up in prison? I\'ve done nothing wrong!\". The mages begins to softly chant {} {} {}. The Wizard and Sorceress, with mysterious expressions, hand you a shimmering USB drive. As they press it into your palm, the mages step aside revealing a door partly ajar. Through the crack in the door, you see a flickering not unlike a late 2013 27-inch iMac LED screen. With a sense of thrill, you slowly walk through the door. Press [enter] to proceed.\n'.format(final_puzzle['Part III']['Answer'], user.name, user.name, user.name), user, color = 'green')
				self.completed = True
				return(self.completed)

			elif user_answer.lower() != final_puzzle['Part III']['Answer']:
				try_counter -= 1
				print_s('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter), color = 'red')

				if try_counter == 0:
					print_s('\nYOU ARE A FAILURE!\n', color = 'red')
					return(self.completed)

	
#==============
# End of Module
#==============		
