#!/usr/bin/env python3

import creatures, random, sass, time, puzzles
from textFormat import print_s, input_s

shark = creatures.Shark()

def shark_game(player):
	dice = random.randint(1,10)
	print_s(shark.art())
	print_s("As you run up the stairs toward the elusive Wizard and onto the balcony, you encounter an escaped 'mythical' creature from the menagerie - the famous talking LandShark")
	time.sleep(2)
	print_s("The clever LandShark, having been on land for so long, has grown lungs and developed tuberculosis (in addition to liver cirrhosis, for other reasons).")
	decision = input_s("Do you [jump over the shark] and risk infection or [go the long way] on your quest to the wizard?")
	
	while str(decision) not in ['jump over the shark', 'go the long way', 'riddle me']:
		decision = input_s(sass.sample_sass(), player)
	
	if decision == "jump over the shark":
		if dice > 3:
			print_s("Damn, you just signed up for a lifetime of suffering, lose 3 HP")
			player.hp -= 3
		elif dice <= 3:
			print_s("You narrowly escaped, but why were you so foolish in the first place?")
			player.intelligence -= 2
			player.hp += 2
	elif decision == "go the long way":
		print_s("Someone knows what they're doing! Good job!")
		player.intelligence += 3
		
	elif decision == "riddle me":
		print_s("Congrats! *coughs violently* You have uncovered my hidden riddle!")
		my_puzzle = puzzles.Puzzles()
		puzzle_success = my_puzzle.do_puzzle(user = player)
        if puzzle_success == True:
        	print_s("Great work! You completed my riddle and are richly rewarded.")
			player.intelligence += 3
			player.attack += 2
		else puzzle_success == False:
			print_s("Drats, you failed. But (cough) have a free pass anyway.")
			