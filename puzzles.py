#!/usr/bin/env python3

#Puzzles and side-quests class

import re
import random 
import user

class Puzzles(object)

	def __init__(self, puzzle_type = None, completed = False):
		self.puzzle_type = puzzle_type
		self.completed = completed

#=====================================
#Creating nested dictionary of puzzles
#=====================================

master_puzzles = {
		'Puzzle 1': {
				'Question:':'xxxx',
				'Answer:'  :'yyyy'
		}
		'Puzzle 2': {
				'Question:':'zzzz',
				'Answer:'  :'qqqq'
		}
		'Puzzle 3': {
				'Question:':'aaaa',
				'Answer:'  :'bbbb'
		}
}	

#====================================
#Function that intakes user input
#from command line (yes or no)
#If yes, user enters if statement, a 
#puzzle gets printed to the screen,
#and user is prompted to enter answer
#====================================
							
	def do_puzzle(self, user_input = None, puzzle_question = None )
		try_counter = 3
		if user_input == upper('yes'):
			puzzle_question = random.choice(list(master_puzzles))
			print(master_puzzles[puzzle_question]['Question:'])
#user needs to imput answer to command line
			if user_answer == master_puzzles[puzzle_num]['Answer:']:
				print('{} is correct! You may proceed.'.format(master_puzzles[puzzle_num]['Answer:']))
			else user_answer != master_puzzles[puzzle_num]['Answer:']:
				try_counter -= 1
				print('{} is incorrect! You have {} more tries.'.format(user_answer, try_counter) 
				if try_counter = 0:
					print('You have {} tries left. You have failed and are now dead.'.format(try_counter))

		 

		
