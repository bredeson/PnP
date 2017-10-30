#!/usr/bin/env python3

import creatures, sass
from textFormat import print_s, input_s

art = '''

                  (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   ( _   /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
'''

def first_combat(player):
    first_combat_query=input_s("You hear the heavy footfalls of an approaching hulking guard.\
 The only way to avoid confronting it is to go down the stairs. Do you [stay and fight] or [go down the stairs]?\n", player)
    if first_combat_query=="go down the stairs":
        print_s("Darwin would be proud.\n")
        decision_counter=0
    elif first_combat_query=="stay and fight":

        print(art)
        opponent=creatures.Creatures(name="hulking guard", hp=30, attack=8) #initializing creature. Might need to update if creatures updates.

        player.combat(opponent)
        decision_counter=2
    else:
        print_s(sass.sample_sass(), color='purple')
    return(decision_counter)
    
