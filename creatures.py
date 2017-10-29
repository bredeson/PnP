#!/usr/bin/env python3

import re, sys, time, random
from random import randrange

creature_dict = {}
level1_dict = {}
level2_dict = {}

# random_creature = None

# Generates a generic class "Creatures" with three attributes with defaults:
# Name, HP (health), and Attack (as a stat/property - treat as noun).
class Creatures:
    def __init__(self, name = "zebrafish", hp = 5, attack = 8, stage = 'level1'):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stage = stage
    def art(self):
    	return '''       
                  __,
               .-'_-'`
             .' {`
         .-'````'-.    .-'``'.
       .'(0)       '._/ _.-.  `\
      }     '. ))    _<`    )`  |
       `-.,\'.\_,.-\` \`---; .' /
            )  )       '-.  '--:
           ( ' (          ) '.  \
            '.  )      .'(   /   )
              )/      (   '.    /
                       '._( ) .'
                           ( (
                            `-.

'''
    	
# Add "art" method. Return ASCII with this method.
	
# Generating a creatures dictionary from a provided text file - prevents manual coding of \
# individual creatures to make things easier and expansion straightforward.

# Entries in dictionary file must be:
# Tab-delimited
# Value will have two values and an optional third:
	# Name
	# HP
	# Attack (Damage)
	## ALWAYS IN THAT ORDER ##
	
class Goblin(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = "Goblin", hp = 10, attack = 6)
	def art(self):
		return """
					 ,      ,
					/(.-""-.)\
				|\  \/      \/  /|
				| \ / =.  .= \ / |
				\( \   o\/o   / )/
				 \_, '-/  \-' ,_/
				   /   \__/   \
				   \ \__/\__/ /
				 ___\ \|--|/ /___
			   /`    \      /    `\
			  /       '----'       \
  """
	
class HulkingGuard(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Hulking Guard', hp = 7, attack = 5)
	def art(self):
		return '''
		
                                 _A_
                                / | \
                               |.-=-.|
                               )\_|_/(
                            .=='\   /`==.
                          .'\   (`:')   /`.
                        _/_ |_.-' : `-._|__\_
                       <___>'\    :   / `<___>
                       /  /   >=======<  /  /
                     _/ .'   /  ,-:-.  \/=,'
                    / _/    |__/v^v^v\__) \
                    \(\)     |V^V^V^V^V|\_/
                     (\\     \`---|---'/
                       \\     \-._|_,-/
                        \\     |__|__|
                         \\   <___X___>
                          \\   \..|../
                           \\   \ | /
                            \\  /V|V\
                             \|/  |  \
                              '--' `--`   
		'''

class SleepingGuard(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Sleeping Guard', hp = 4, attack = 3)
	def art(self):
		return '''
                z 
                         z 
                          Z 
                .--.  Z Z 
               / _(c\   .-.     __  
              | / /  '-;   \--'`  `\______ 
              \_\/'/ __/ )  /  )   |      \--, 
              | \`""`__-/ .'--/   /--------\  \ 
               \`\  ///-\/   /   /---;-.    '-' 
                            (________\  \ 
                                      '-' 
'''

class Ogre(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Ogre', hp = 15, attack = 8)
	def art(self):
		return '''
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo
		'''

class Simon(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Simon the Python', hp = 9, attack = 4)
	def art(self):
		return '''
	   __
      {0O}
      \__/
      /^/
     ( (              
     \_\_____
     (_______)
    (_________()Oo
'''

class C57BL6(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Mouse', hp = 7, attack = 3)
	def art(self):
		return '''
					 .--,       .--,
					( (  \.---./  ) )
					 '.__/o   o\__.'
						{=  ^  =}
						 >  -  <
						/       \
					   //       \\
					  //|   .   |\\
					  "'\       /'"_.-~^`'-.
						 \  _  /--'         `
					   ___)( )(___
					  (((__) (__)))
'''

class Mage(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Mage', hp = 20, attack = 15)
	def art(self):
		return '''
                    ____
                  .’* *.’
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ‘ \(((()))/ ‘
            / ‘ \)).))/ ‘ \
           / _ \ - | - /_  \
          (   ( .;’’’;. .’  )
          _\”__ /    )\ __”/_
            \/  \   ‘ /  \/
             .’  ‘...’ ‘ )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .’   /    b    ‘.  ‘.
     _.-’    /     Bb     ‘-. ‘-._
 _.-’       |      BBb       ‘-.  ‘-.
(________mrf\____.dBBBb.________)____)
	
		'''

class Soapberry(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Red-Shouldered Soapberry', hp = 4, attack = 2)
	def art(self):
		return '''
		                    :                                
                          `o                                
                          /:                                
                          s`                                
                          y                                 
                         `s                                 
                         ./                                 
``                       -/                                 
 -///:`                  :/  `/                             
     `:///-              -+   y                             
          .:--.          `s   m                             
              ://.        y   h.                            
                 ://`     o+  ./-                           
                   `:o-`sdyd/.` .o`                         
           .+::`     `+omNNNNms -mo     ..                  
              .+o+`   `hmNNNNNmmmh`    :moy`                
                 `:-  `+hmNmNNNmmmy/. -m+ `y`               
                   `/ssohNNNmNNmNmmmhsds   -s               
                     .-:+dmmmmNNNNNNNNNh:   +o              
                        .ymNNNNNNNmmNNNmms`  ys-:::/:.      
                   /o+/-`+hNNNmNNmNNNNNNmNd-  `...          
                  `h:/+shyNNNNNNmNNNNNNNNNNmdhhhhhdddhy-    
                   .s`    ymmNNNNNNNNNNNNNNNN+     ``./h    
                    `s-   `dmmNNNNNNNNNNNNNNNN+       /+    
                      s+   .dNmmNNNNNNMNNNNNNNN/      y-    
                       ys   -NNNNNNNNNNMMNNNNNNN/    `m     
                      `s-  :msdNNNNNNNNNNMNMNNNNN/   :s     
                     :+.  /mo `sNNNNNNNNNNNNNNNNNm.  s/     
                    :.   +mo    /mNNNNNNNNNNNNNNMMs  m.     
                        +Ns      .dNNNNNNNNNNNNNNNh -N      
                       .Ny        `sNNNMNNNNNNNNNNN`oh      
                        -+++:`      :dNNNNNNNNNNNNN. +o/    
                            ./oo+:`   -odNNNNNNNNNm    :+/. 
                                 -+ss+:` :yNNNNNNm+       o`
                                     ./sh/  -/+o/.          
                                         d                  
                                         d.                 
                                         y                  
                                         s                  
'''

class Sheep(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Sheep', hp = 12, attack = 2)
	def art(self):
		return '''
		   __  _
       .-.'  `; `-._  __  _
      (_,         .-:'  `; `-._
    ,'o"(        (_,           )
   (__,-'      ,'o"(            )>
      (       (__,-'            )
       `-'._.--._(             )
          |||  |||`-'._.--._.-'
                     |||  |||

'''

class Capuchin(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'White-Faced Capuchin', hp = 8, attack = 8)
	def art(self):
		return '''
       .="=.
     _/.-.-.\_     _
    ( ( o o ) )    ))
     |/  "  \|    //
      \'---'/    //
      /`"""`\\  ((
     / /_,_\ \\  \\
     \_\\_'__/ \  ))
     /`  /`~\  |//
    /   /    \  /
,--`,--'\/\    /
 '-- "--'  '--'
'''

class Oyster(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Oyster', hp = 30, attack = 3)
	def art(self):
		return '''
		   _.---._
       .'"".'/|\`.""'.
      :  .' / | \ `.  :
      '.'  /  |  \  `.'
       `. /   |   \ .'
         `-.__|__.-'
         '''

creature_dict['goblin'] = Goblin
creature_dict['sleepyguard'] = SleepingGuard
creature_dict['hulkingguard'] = HulkingGuard
creature_dict['oyster'] = Oyster
creature_dict['capuchin'] = Capuchin
creature_dict['sheep'] = Sheep
creature_dict['soapberry'] = Soapberry
creature_dict['mage'] = Mage
creature_dict['mouse'] = C57BL6
creature_dict['ogre'] = Ogre

# creatures_list = open('sample_creatures_list', 'r')
# creature_dict = {}
# for line in creatures_list:
# 	split = line.strip().split('\t')
# 	creature_dict[split[0]] = split[1]	
# for key, value in creature_dict.items():
# 	creature_dict[key] = value.split(',')

# Random selection of creatures for each call of the class - needs to be acknowledged in backbone.

def Random():
	random_creature = random.choice(list(creature_dict))
	random_creature_constructor = creature_dict[random_creature]
	return random_creature_constructor()

		# if type is not None:
		# 	random_creature = type
		# else:
		#	random_creature = random.choice(list(creature_dict))
		#self.name = creature_dict[str(random_creature)][0]
		#self.hp = int(creature_dict[str(random_creature)][1])
		#self.attack = int(creature_dict[str(random_creature)][2])

# Drew has taken care of the random attack value selection - excellent.

# Better to use a generic creature class 