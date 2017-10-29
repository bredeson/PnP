#!/usr/bin/env python3

import user, textwrap

#==========================================
#Custom print functions and status output
#==========================================

color_dict = {'purple' : '\033[95m',
			  'blue' : '\033[94m',
			  'green' : '\033[92m',
			  'yellow' : '\033[93m',
			  'red' : '\033[91m',
			  'end' : '\033[0m',
			  'bold' : '\033[1m',
			  'underline' : '\033[4m'}

def printHealthBar (current_hp, starting_hp, decimals = 1, length = 50, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (current_hp / starting_hp))
    filledLength = int(length * current_hp // starting_hp)
    bar = fill * filledLength + '-' * (length - filledLength)
    bar_out = '|{}| {}%'.format(bar, percent)
    return(bar_out)


def input_s(text, user, color = ''):
	if not color == '':
		color_code = color_dict[color]
		query= input(color_code + text + color_dict['end'])
	else:
		query= input(text)
		query = textwrap.fill(query)
	while query=="status":
		color_code = color_dict['green']
		print(color_code + "\nName: {}\nHealth Points: {}\nDifficulty: {}\nAttack: {}\n".format(user.name, printHealthBar(user.hp, user._hp), user.difficulty, user.attack) + color_dict['end'])
		query=input(text)
	return(query)

def print_s(text,color = ''):
	text = textwrap.fill(text)
	if not color == '':
		color_code = color_dict[color]
		print(color_code + text + color_dict['end'])
	else:
		print(text)
