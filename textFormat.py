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
			  'underline' : '\033[4m',
			  'blink' : '\033[5m',
			  'dim' : '\033[2m'}

def printHealthBar (current_hp, starting_hp, decimals = 1, length = 50, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (current_hp / starting_hp))
    filledLength = int(length * current_hp // starting_hp)
    if current_hp < 5:
    	bar = color_dict['blink'] + color_dict['red'] + fill * filledLength + color_dict['end'] + color_dict['blink'] + color_dict['dim'] + fill * (length - filledLength) + color_dict['end'] + color_dict['green']
    	bar_out = '{}hp|{}| {}%'.format(current_hp, bar, percent)
    else:
    	bar = fill * filledLength + color_dict['end'] + color_dict['dim'] + fill * (length - filledLength) + color_dict['end'] + color_dict['green']
    	bar_out = '{}hp|{}| {}%'.format(current_hp, bar, percent)
    return(bar_out)

def print_s(text,color = ''):
	text = textwrap.fill(text, replace_whitespace = False, drop_whitespace = False)
	if not color == '':
		color_code = color_dict[color]
		print(color_code + text + color_dict['end'])
	else:
		print(text)

def input_s(text, user=None, color = '', recurse = False):
	if recurse is False:
		text += '\n> '
	if not color == '':
		color_code = color_dict[color]
		query= input(textwrap.fill(color_code + text + color_dict['end'], replace_whitespace = False, drop_whitespace = True))
	else:
		query= input(textwrap.fill(text, replace_whitespace = False, drop_whitespace = True))
	while query=="status":
		color_code = color_dict['green']
		print(color_code + "\nName: {}\nLevel: {}\nHealth Points: {}\nDifficulty: {}\nAttack: {}\nMana: {}\nIntelligence: {}\n".format(user.name, user.level, printHealthBar(user.hp, user.hpmax), user.difficulty, user.attack, user.mana, user.intelligence) + color_dict['end'])
		query=input_s(text, user, color = color, recurse = True)
	return(query)

