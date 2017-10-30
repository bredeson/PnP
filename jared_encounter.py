#!/usr/bin/env python3

import creatures, random, sass, time, puzzles
from textFormat import print_s, input_s

# Shit I need for testing?
import user
player = user.Prisoner(name = 'Jared', difficulty = 'easy') 

shark = creatures.Shark()

def shark_game(player):
	dice = random.randint(1,10)
	print(shark.art())
	print_s("As you run up the stairs toward the elusive Wizard and onto the balcony, you encounter an escaped 'mythical' creature from the menagerie - the famous talking LandShark")
	time.sleep(2)
	print_s("The *clever* LandShark, having been on land for so long, has grown lungs and developed consumption (in addition to liver cirrhosis, for other reasons).")
	decision = input_s("Do you [jump over the shark] and risk infection or [go the long way] on your quest to the wizard?", user = player)

	while str(decision) not in ['jump over the shark', 'go the long way', 'riddle me']:
		decision = input_s(sass.sample_sass(), user = player, color="purple")

	if decision == "jump over the shark":
		if dice > 3:
			print_s("Damn, you just signed up for a lifetime of pain and suffering, lose 3 HP")
			player.hp -= 3
		elif dice <= 3:
			print_s("You narrowly escaped, but why were you so foolish in the first place? Dumbass.")
			player.intelligence -= 2
			player.hp += 2
		
	elif decision == "go the long way":
		print_s("Someone knows what they're doing! Good job!")
		player.intelligence += 3
		print_s("Now you have to double back to the stairs to find an alternative route and encounter the legendary, award winning Milwaukee's Best (Monster)")
		beer = creatures.Beer()
		print(beer.art())
		print_s("To get past this monster, you must fight one of his (somewhat drunken) creatures")
		time.sleep(2)
		animal = creatures.Animals()
		print(animal.art())
		print_s("A wobbly " + animal.name + " stumbles down the stairs and attacks!\n")
		player.combat(animal)
	
		if player.hp>0:
			print_s("I hope you're proud of your self, defeating a drunken " + animal.name + ". But you get to pass on to your greatest challenge yet. \n")
			fake_query=input_s("", player)
		
	elif decision == "riddle me":
		print_s("Congrats! *coughs violently* You have uncovered my hidden riddle!")
		my_puzzle = puzzles.Puzzles()
		puzzle_success = my_puzzle.do_puzzle(user = player)
	
		if puzzle_success == True:
			print_s("Great work! You completed my riddle and are richly rewarded.")
			player.intelligence += 3
			player.attack += 2
		
		elif puzzle_success == False:
			print_s("Drats, you failed. But (cough) have a free pass anyway.")
		
