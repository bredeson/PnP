#!/usr/bin/env python3

#=============================
#Puzzles and side-quests class
# By Shasta Webb
# 28 October 2017
# filename = puzzles.py
#=============================

#=================
#Required modules:
# 1) random
# 2) os
# 3) sass
# 4) user
# 3) textFormat
#=================

import user
import random 
import sass
import os
from textFormat import print_s, input_s

#=====================================
#Creating nested dictionary of puzzles
#=====================================

master_puzzles = {
		'Puzzle 1': {
				'Question:':'What is harder to catch the faster you run?',
				'Answer:'  :'breath',
				'Hint:'	   :'Inhale, exhale, inhale.'	
		},
		'Puzzle 2': {
				'Question:':'When was the latest year that is the same upside down?',
				'Answer:'  :'1961',
				'Hint:'    :'Try writing it out.'
		},
		'Puzzle 3': {
				'Question:':'A thief enters a shop and threatens the clerk, forcing him to open the safe. The clerk says, "The code for the safe is different every day, and if you hurt me you\'ll never get the code". But the thief manages to guess the code on his own. What is the code?',
				'Answer:'  :'different',
				'Hint:'    :'Think about the WORDS.'
		},
		'Puzzle 4': {
				'Question:':'What word becomes shorter when you add two letters to it?',
				'Answer:'  :'short',
				'Hint:'    :'len(short) >= len(shorter)?.'
		},
		'Puzzle 5': {
				'Question:':'What was the world’s highest mountain before the discovery of Everest?',
				'Answer:'  :'everest',
				'Hint:'    :'Can heights of mountains change?'
		}
}		

#========================
#Creating a class Puzzles
#========================

class Puzzles(object):

	def __init__(self, puzzle_question = None, completed = False):
		self.puzzle_question = random.choice(list(master_puzzles))
		self.completed = completed

#========================================================
#Function that intakes user input
#from command line (yes or no)
#If yes, user enters if statement, a 
#puzzle gets printed to the screen,
#and user is prompted to enter answer
#Usage:
#	user_input = [yes] or [no] from command line
#	user_answer = string from command line
#	puzzle_question = generated within function, no 
#						input from command line necessary
#========================================================

#========================================================
#To use puzzles in the backbone script, you need to:
# 1) intitialize a puzzle object
#		my_puzzle = puzzle.Puzzle()
# 2) call do_puzzle function with player as input
#		my_puzzle.do_puzzle(player)
#========================================================
							
	def do_puzzle(self, user_input = None, user = None):
		try_counter = user.intelligence
		user_input = input_s('Time for a puzzle! Are you up to the task? [yes] or [no]\n\n', user)
		while user_input not in ['yes', 'no']:
			user_input = input_s('Invalid response. Enter [yes] or [no]\n\n', color = 'purple') 

		if user_input == 'yes':
			print_s(master_puzzles[self.puzzle_question]['Question:']) 
			
			while try_counter > 0:
				user_answer = input_s('What is your answer?\n', user)
		
				if user_answer.lower() == master_puzzles[self.puzzle_question]['Answer:']:
					print_s('\n {} is correct! You may proceed.'.format(master_puzzles[self.puzzle_question]['Answer:']), color = 'green')
					del master_puzzles[self.puzzle_question]
					self.completed = True
					return(self.completed)

				elif user_answer.lower() != master_puzzles[self.puzzle_question]['Answer:']:
					try_counter -= 1
					print_s('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter), color = 'red') 

					if try_counter > 0:
						user_hint = input_s('Are you maybe a little bit dumb? Perhaps you drank a little too much Farmer Nick\'s Ancient Grain Sorghum Whiskey? Would you like a hint? [yes] or [no]', user)

						while user_hint not in ['yes', 'no']:
							user_hint = input_s('Invalid response. Enter [yes] or [no].\n\n', user, color = 'purple')
				
						if user_hint == 'yes':
							print_s(master_puzzles[self.puzzle_question]['Hint:'])
						
					if try_counter == 0:
						print_s('Guess what? You failed. You\'re fucked.', color = 'red')
						self.completed = False
						return(self.completed)

		elif user_input == 'no':
			print_s('That was probably a mistake. Best of luck, though.', color = 'red')
			return(self.completed)


#=============
#End of module
#=============
		 

		
