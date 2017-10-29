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
#=================

import re
import random 
#import sass
import os

#=====================================
#Creating nested dictionary of puzzles
#=====================================

master_puzzles = {
		'Puzzle 1': {
				'Question:':'What is the latin name for white-faced capuchin monkey?',
				'Answer:'  :'Cebus capucinus imitator'
		},
		'Puzzle 2': {
				'Question:':'What is 4 + 3?',
				'Answer:'  :'7'
		},
		'Puzzle 3': {
				'Question:':'What day is it?',
				'Answer:'  :'Saturday'
		},
		'Puzzle 4': {
				'Question:':'q'
				'Answer:'  :'t'
		},
		'Puzzle 5': {
				'Question:':'a'
				'Answer:'  :'b'
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
							
	def do_puzzle(self, user_input = None):
		try_counter = 3
		user_input = input('Would you like to do a puzzle? If you say [no], you will lose only X hp. If you say [yes], you could strike it rich, but if you fail, it could mean danger!\n\n')
		while user_input not in ['yes', 'no']:
			user_input = input('invalid. try again.\n\n') 

		if user_input == 'yes':
			print(master_puzzles[self.puzzle_question]['Question:']) 
			
			while try_counter > 0:
				user_answer = input('What is your answer?\n')
		
				if user_answer == master_puzzles[self.puzzle_question]['Answer:']:
					print('\n{} is correct! You may proceed.'.format(master_puzzles[self.puzzle_question]['Answer:']))
					del master_puzzles[self.puzzle_question]
					self.completed = True
					return(self.completed)

				elif user_answer != master_puzzles[self.puzzle_question]['Answer:']:
					try_counter -= 1
					print('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter)) 
					
					if try_counter == 0:
						print('You have {} tries left. Guess what? You\'re fucked.'.format(try_counter))
						self.completed = False
						return(self.completed)

#=============
#End of module
#=============
		 

		
