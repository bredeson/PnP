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
				'Question':'This is question 1.',
				'Answer'  :'1',
				'Hint'    :'1'
		},
		'Part II': {
				'Question':'This is question 2.',
				'Answer'  :'2',
				'Hint'    :'2'
		},
		'Part III' {
				'Question':'This is question 3.'
				'Answer'  :'3',
				'Hint'    :'3'
		}
}

#=================================
# Definining final_puzzle function  
#=================================

def final_puzzle(user_answer = None, user = None, completed = None)
	print_s(wizard.art(), color = 'purple')
	try_counter = user.intelligence
	print_s('\n\nYou walk through the door to the highest room in the highest tower. Your stomach churns a bit from the oysters and whiskey you might have consumed. Despite the drinking, the dodgy oysters, the sewer, and other distastful experiences, you\'ve somehow made it to the end. You encounter a wizard named Simon and his band of mages. Before you can win Simon\'s respect, you have one last challenge. Press [Enter] to proceed.\n\n')
	
#====================
# Final Puzzle Part I
#====================	
	
	while try_counter > 0:
		user_answer = input_s('\n\n' + final_puzzle['Part I']['Question'], user) 
		
		if user_answer.lower() == final_puzzle['Part I']['Answer']:
			try_counter = user.intelligence
			proceed = input_s('\n{} is correct! You may proceed. Press [enter] to proceed.\n'.format(master_puzzles[self.puzzle_question]['Answer:']), color = 'green')

		elif user_answer.lower() != final_puzzle['Part I']['Answer:']:
			try_counter -= 1
			print_s('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter), color = 'red')

			if try_counter == 0:
				print_s('Guess what? You failed. You\'re fucked.', color = 'red')
				completed = False
				return(completed)

#=====================
# Final Puzzle Part II
#=====================

	print_s('You\'ve managed to make it to Part II, and you\'re that much closer to gaining Wizard Simon and Sorceress Sofia\'s respect. But you have two more challenged ahead. Good luck!')

	while try_counter > 0:			
		user_answer = input_s('\n\n' + final_puzzle['Part II']['Question'], user)

		if user_answer.lower() == final_puzzle['Part II']['Answer']:
			try_counter = user.intelligence
			proceed = input_s('\n{} is correct! You may proceed. Press [enter] to proceed.\n'.format(master_puzzles[self.puzzle_question]['Answer:']), color = 'green')

		elif user_answer.lower() != final_puzzle['Part II']['Answer:']:
			try_counter -= 1
			print_s('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter), color = 'red')

			if try_counter == 0:
				print_s('Guess what? You failed. You\'re fucked.', color = 'red')
				completed = False
				return(completed)

#======================
# Final Puzzle Part III
#======================
			
	while try_counter > 0:			
		user_answer = input_s('\n\n' + final_puzzle['Part III']['Question'], user)

		if user_answer.lower() == final_puzzle['Part III']['Answer']:
			try_counter = user.intelligence
			proceed = input_s('\n{} is correct! You may proceed. Press [enter] to proceed.\n'.format(master_puzzles[self.puzzle_question]['Answer:']), color = 'green')
			completed = True
			return(completed)

		elif user_answer.lower() != final_puzzle['Part III']['Answer:']:
			try_counter -= 1
			print_s('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter), color = 'red')

			if try_counter == 0:
				print_s('Guess what? You failed. You\'re fucked.', color = 'red')
				completed = False
				return(completed)

	
		
