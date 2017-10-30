#!/usr/bin/env python3

import creatures, random
from textFormat import print_s, input_s

opponent = creatures.SleepingGuard()

def second_combat(player):

    print(opponent.art())
        
    d_10 = random.randint(1,10)
    
    if d_10 > 3:
        print_s("Sneaky sneaky... you did it.\n")
        decision_counter = 0
    
    elif d_10 <= 3:
        print_s("Oh snap, you woke him up you club footed moose. \n", color='purple')
        player.combat(opponent)
        decision_counter = 2
    
    return(decision_counter)
