#!/usr/bin/env python3

import re, sys, time, random
from random import randrange

master_dict = {}
level1_dict = {}
level2_dict = {}
animals_dict = {}

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
		Creatures.__init__(self, name = 'Hulking Guard', hp = 12, attack = 8)
	def art(self):
		return '''
	    
                                 _A_						
                                / | \						
                               |.-=-.|						
                               )\_|_/(						
                            .==’\   /`==.						
                          .’\   (`:’)   /`.						
                        _/_ |_.-’ : `-._|__\_					
                       <___>‘\    :   / `<___>					
                       /  /   >=======<  /  /						
                     _/ .’   /  ,-:-.  \/=,’						
                    / _/    |__/v^v^v\__) \						
                    \(\)     |V^V^V^V^V|\_/						
                     (\\     \`---|---’/						
                       \\     \-._|_,-/							
                        \\     |__|__|							
                         \\   <___X___>							
                          \\   \..|../							
                           \\   \ | /							
                            \\  /V|V\									
                             \|/  |  \								
                              ‘--’ `--`   								
		'''

class NobleGuard(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Noble Guard', hp = 12, attack = 8)
	def art(self):
		return '''
  ,^.
  |||
  |||       _T_
  |||   .-.[:|:].-.
  ===_ /\|  “‘“  |/
   E]_|\/ \--|-|’’’’|
   O  `’  ‘=[:]| A  |
          /””””|  P |
         /”””””`.__.’
        []”/”””\”[]
        | \     / |
        | |     | |
      <\\\)     (///>
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
                  o        __,='`````'=/__									
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
                        ooOO(_)    (_)OOo 										
        '''

# class Simon(Creatures):
# 	def __init__(self):
# 		Creatures.__init__(self, name = 'Simon the Python', hp = 9, attack = 4)
# 	def art(self):
# 		return '''
#        __
#       {0O}
#       \__/
#       /^/
#      ( (              
#      \_\_____
#      (_______)
#     (_________()Oo
# '''

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
                  .'* *.'								
               __/_*_*(_									
              / _______ \								
             _\_)/___\(_/_									
            / _((\- -/))_ \									
            \ \())(-)(()/ /									
             ' \(((()))/ '									
            / ' \)).))/ ' \								
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
		Creatures.__init__(self, name = 'Red-Shouldered Soapberry Bug', hp = 4, attack = 2)
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

class Clown(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'the Clown', hp = 25, attack = 18)
	def art(self):
		return '''
       ,            _..._            ,									
      {'.         .'     '.         .'}											
     { ~ '.      _|=    __|_      .'  ~}									
    { ~  ~ '-._ (___________) _.-'~  ~  }									
   {~  ~  ~   ~.'           '. ~    ~    }										
  {  ~   ~  ~ /   /\     /\   \   ~    ~  }									
  {   ~   ~  /    __     __    \ ~   ~    }									
   {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}									
    { ~   ;(      \/ .-. \/      );   ~ }									
     { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }									
      '-._~ \   (`-._'-'_.-')   / ~_.-'									
          '--\   `'._'"'_.'`   /--'											
              \     \`-'/     /  											
               `\    '-'    /'   										
                 `\       /'    									
                   '-...-'												
'''

class Oyster(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'the Oyster', hp = 30, attack = 3)
	def art(self):
		return '''
           _.---._
       .'"".'/|\`.""'.
      :  .' / | \ `.  :
      '.'  /  |  \  `.'
       `. /   |   \ .'
         `-.__|__.-'
         '''

class Python(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Python (Monty)', hp = 35, attack = 8)
	def art(self):
		return '''
                    uJ$$$$$$',J <$$h.                  .,J+.
                 ,J$$$$$$$"z$F,J$$??$$h- =<$$C$$$>-.zJ"J?? $$ccc,.
               .r$$$$$$$$$$$$$$$$$F "?$$$hJ$$$$$'zJ$$$P" ,$z$$P$$F$hu
              J$h?$$$$$$$$$$$$$$$$$$$. ``$$$$$$$$$$$"" ,J$x$$$<$$L$$$N
            .P$$$$F"""   ' `"??$$$h?$$$ucd$$$$$$$$$hcr$P"J?$$P""??$Lc$F
            J$JF                `?$C`?$$$$$$"$"$$$$$$P",JP"       `$$$F
            ?$F                   `?h..`"?$$$$$$$F" .,zP           $$$$
            cc         u  ..        `$$P   `""""  J$$"   -c    "   $$$F
            ?F       ,$ z$$$,ccu.,.  `?$h        ,J$'.    $    .  ,$$F
            ;h       ????$$$$$$$$$$$u   "h. p"  u$" JF   =     " ;PP"
            `?      <$hcr. `"""????$$r   `;d"  ,$" `"           JP"
             $r      $$$$$$$$$$hccccc   ,P",, ,P" J$$$       .P"
              ?      """""""???"      ,p"   """  J$$P"     >'
               `c     hcc,,.      -=="F          "      uF
                `=    `?$$$$-<$$h    j'      .,J$$$  .'"
                  `\.    ""?h.`$$$C  "     z$$$P"   $$"
                     "  .   .`""""""     ,cL..,,,cc,h
                       `"$h,`$$$$$F ?$C `$$$$$$$$""<$
                          "?hu`"?$$F $$h. `???"  .. ?
                             "?hu cccccccccd$$$$$$$$
                                "?h."$$$$$$$$$$????"
                                  `?hu` zccccccd$$$$$$u
                                     `"h,"?$$$$$$$$$??""
                                        `?h.' .;ccccd$$$$$c
                                           "$h."$$$$$$$$$$$$c
                                             "$h.?$$$??????""
                           .,zcccccccccccu.   `?$u ,cc$$$$$$$$$c
             ,cc$$$P",cd$$$$$$$$$$$$P"""".zc$$$,?$h $$$$$$$$$$$$.
         ,J$$$$P",cd$$$$$$$$??"".,ccd$$$$$$$$$$$ $$h`"""""".,,,,,
h      ;J$$$P",c$$$$$$?"",ccc$$$$$$$$$$$$$$$$$$$ $$$ $$$$$$$$$$$$
`$    x$$?",d$$$$?",cd$$$$$$$$$$$$$$$$$P". .  .`;$$',$$$$$$$$$$$F;,
 ?h.__,zc$$??",cd$$$$$$$$$$$$$$$$$P" zc<$$'$F',J$$F,cccccccccccc J$$$u
  `"""""",zc$$$$$$$$$$$$$$$$$P"",;J$r"" ",uccd$$$F J$$$$$$$$$$P J$$$$$h
      `$$$$$$$$$$$$$$$$$??",zc $$F .uJ$$$$$$$$$P'..""""""""""",$$$$$$$$
        "?$$$$$$$??""",cr$$??""'c$$$$$$$$$$$$P" <$$$$$$$$$$",J$$$$$$$P"
                `"`?? ??"      `"?$$$$$$$$$",ccc,.```"???".,c,""?CLz>
                                    "??""' J$$$$$$$$$$"  ?????????"
'''

class Harry(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Harry Potter', hp = 25, attack = 10)
	def art(self):
		return '''
            _            _.,----,								
 __  _.-._ / ‘-.        -  ,._  \) 									
|  `-)_   ‘-.   \       / < _ )/” }										
/__    ‘-.   \   ‘-, ___(c-(6)=(6)										
 , `’.    `._ ‘.  _,’   >\    “  )										
 :;;,,’-._   ‘---’ (  ( “/`. -=’/										
;:;;:;;,  ‘..__    ,`-.`)’- ‘--’										
;’;:;;;;;’-._ /’._|   Y/   _/’ \										
      ‘‘‘“._ F    |  _/ _.’._   `\										
             L    \   \/     ‘._  \											
      .-,-,_ |     `.  `’---,  \_ _|									
      //    ‘L    /  \,   (“--’,=`)7										
     | `._       : _,  \  /’`-._L,_’-._											
     ‘--’ ‘-.\__/ _L   .`’         ‘.//										
                 [ (  /													
                  ) `{													
                  \__)													
                  
'''

class Wizard(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'the Wizard', hp = 25, attack = 10)
	def art(self):
		return '''
              o												
                   O       /`-.__   								
                          /  \·’^|          						
             o           T    l  *								
                        _|-..-|_       									
                 O    (^ ‘----’ `)								
                       `\-....-/^     								
             O       o  ) “/ “ (									
                       _( (-)  )_      									
                   O  /\ )    (  /\ 									
                     /  \(    ) |  \   									
                 o  o    \)  ( /    \										
                   /     |(  )|      \ 									
                  /    o \ \( /       \									
            __.--’   O   SIMON   .._   \									
           //|)\      ,   (_)   /(((\^)’\										
              |       | O         )  `  |									
              |      / o___      /      /									
             /  _.-’’^^__O_^^’’-._     /									
           .’  /  -’’^^    ^^’’-  \--’^										
         .’   .`.  `’’’----’’’^  .`. \										
       .’    /   `’--..____..--’^   \ \										
      /  _.-/                        \ \									
  .::’_/^   |       Programming        |  `.										
         .-’|           for            |    `-.										
   _.--’`   \         Biology         /       `-.									
  /          \         2017          /           `-._								
  `’---..__   `.                  .´_.._   __       \								
           ``’’’`.              .’gnv   `’^  `’’---’^								
                  `-..______..-’													
'''
		
class Sorceress(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'the Duchess of Blackford Hall', hp = 25, attack = 10)
	def art(self):
		return '''

                       `;.`;'.
                     `;);.(~;(`;
                   `(;);;;;;);(::`
                    ;)(; ; ;;~;;;(;
                  `(`;;~-  -~(;~;)`)
                  ;(`;)      ;);;; ;
                `;);;(;`\ ^_/(;)~;;);
                  (;);.;)   ':);( ..(;
                  `'((;);   )(.');`:
                   |.' );)`   ); ;`.)
                   |  |(   ) (  ;);:
                *  \  \ \WWWwWWW/;`'
                    \  \ ) .X. (
                 )   \  /  .X.  \   )
                ( (  )`/   /^\   | ( (
                 ) )   |\_/WWW\_/|  ) )
                (   )  | : |\   :\ ( ( *
                 ) ( ( wwwww wwwwww )  )
             * (    )) :::::  :::::(   (
                ) )((  ::::'   ::::. (  )
               ) (   ) ::::'(  ::::( ))   )
              ((    ( ::::' ))::::') )( (
            ( ) ) (  )  )  (( )(  ( (  ) )TS
          ((()))())((()())()()((())()())()()))

'''
		
class Troll(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = 'Troll', hp = 25, attack = 10)
	def art(self):
		return '''
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
'''

class Shark(Creatures):
	def __init__(self):
		Creatures.__init__(self, name = "Renegade Shark", hp = 100, attack = 50)
	def art(self):
		return'''
 _________         .    .
(..       \_    ,  |\  /|
 \       O  \  /|  \ \/ /
  \______    \/ |   \  / 
     vvvv\    \ |   /  |
     \^^^^  ==   \_/   |
      `\_   ===    \.  |
      / /\_   \ /      |
      |/   \_  \|      /
             \________/
'''
	
master_dict['goblin'] = Goblin
master_dict['oyster'] = Oyster
master_dict['capuchin'] = Capuchin
master_dict['sheep'] = Sheep
master_dict['soapberry'] = Soapberry
master_dict['mage'] = Mage
master_dict['mouse'] = C57BL6
master_dict['ogre'] = Ogre
master_dict['nobleguard'] = NobleGuard

level1_dict['sleepyguard'] = SleepingGuard
level1_dict['hulkingguard'] = HulkingGuard
level1_dict['capuchin'] = Capuchin
level1_dict['mouse'] = C57BL6
level1_dict['soapberry'] = Soapberry
level1_dict['python'] = Python

level2_dict['mage'] = Mage
# level2_dict['sorceress'] = Sorceress
level2_dict['ogre'] = Ogre
level2_dict['goblin'] = Goblin
level2_dict['troll'] = Troll
level2_dict['harry'] = Harry

animals_dict['capuchin'] = Capuchin
animals_dict['sheep'] = Sheep
animals_dict['soapberry'] = Soapberry
animals_dict['mouse'] = C57BL6
animals_dict['zebrafish'] = Creatures

## What power levels should the creatures have based on level? That would make things easier all around.

# creatures_list = open('sample_creatures_list', 'r')
# creature_dict = {}
# for line in creatures_list:
# 	split = line.strip().split('\t')
# 	creature_dict[split[0]] = split[1]	
# for key, value in creature_dict.items():
# 	creature_dict[key] = value.split(',')

# Random selection of creatures for each call of the class - needs to be acknowledged in backbone.

def Random():
	random_creature = random.choice(list(master_dict))
	random_creature_constructor = master_dict[random_creature]
	return random_creature_constructor()

def Animals():
	animal_creature = random.choice(list(animals_dict))
	animal_creature_constructor = animals_dict[animal_creature]
	return animal_creature_constructor()
	
def Magic():
	magic_creature = random.choice(list(level2_dict))
	magic_creature_constructor = level2_dict[magic_creature]
	return magic_creature_constructor()
	
		# if type is not None:
		# 	random_creature = type
		# else:
		#	random_creature = random.choice(list(creature_dict))
		#self.name = creature_dict[str(random_creature)][0]
		#self.hp = int(creature_dict[str(random_creature)][1])
		#self.attack = int(creature_dict[str(random_creature)][2])

# Drew has taken care of the random attack value selection - excellent.

# Better to use a generic creature class 
