#!/usr/bin/env python3

import creatures, sass, user, time, puzzles
from textFormat import print_s, input_s

shelf = '''
 _________________________________________________________
||-------------------------------------------------------||
||.--.    .-._                        .----.             ||
|||==|____| |H|___            .---.___|""""|_____.--.___ ||
|||  |====|P| |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
|||==|    |E| |   | \         |   |   |_\/_|Black|  | ^ |||
|||  |    |R| | R |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
|||  |    |L| |   |_\ \_( oo )|   |   |    |Magic|  | ^ |||
|||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||
||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
||-------------------------------------------------------||
||-------------------------------------------------------||
||               ___                   .-.__.-===-. .---.||
||              |===| .---.   __   .---| |XX|  P  |_|^^^|||
||            /(|   |_|III|__|''|__|:x:|=|  |  Y  |=| = |||
||           / (|===|+|   |++|  |==|   | |  |  T  | |   |||
||       /\\\/ _(|===|-|   |  |''|  |:x:|=|  |  H  | |   |||
||_____  -\{___(|   |-|   |  |  |  |   | |  |  O  | | = |||
||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|  N  |=|^^^|||
||              `---^-^---^--^--'--^---^-^--^-===-^-^---^||
||-------------------------------------------------------||
||_______________________________________________________||

'''
def easter_egg(player):
	print_s("You scan the room. It appears mostly empty apart from a dusty bookshelf that seems to contain questionably old and outdated textbooks.")
	time.sleep(2)
	decision = input_s('You may not have time for assing about with useless scholarly nonsense, but it may prove fruitful. Do you [leave] or stay and [search]?', player)

	while decision not in ['leave','search']:
		decision=input_s(sample_sass(), player)

	if decision == 'search':
		print_s("You begin scanning the bookshelf for something entertaining and/or educational. An ancient text, bound in thousands year old embossed centaur leather briefly cathces your eye. It's title, 'Mastery of Python and complex systems', reminds you of an ancient teaching you once received. The effects of amnesia are taking their toll, and the memory fades.")
		book_decision = input_s('You question your existence and past life before the prison. Before you break down into an existential crisis, you [leave] the room. Or do you?', player)
		while book_decision not in ['leave','read']:
			decision=input_s(sample_sass(), player)
		if book_decision == 'read':
			print_s('You impulsively decide to read the book about Pythons. Perhaps in some attempt of mastering creature control? However, pulling the book from the shelf, you realise the book is no book at all. Instead, the bookshelf swings open to reveal a secret room',player,color = 'green')
			print_s("Inside, you find ancient texts and writings in languages you barely know the name of. You study them for some time in an attempt to gain some knowledge")
			hidden_room = puzzles.Puzzle()
			room_puzzle = hidden_room.do_puzzle(user = player)

			if room_puzzle == True:
				print_s("After a few hours your hard work pays off and you gain 1 intelligence, and leave the room")
				player.intelligence += 1

			else:
				print_s('Unfortunately your mental capacity is restricted by inactivity from your time in the cell, and you do not solve the mysteries of the ancient texts. You leave the room')