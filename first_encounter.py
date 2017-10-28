#!/usr/bin/env python3

import creatures

def first_combat(player):
    first_combat_query=input("You hear the heavy footfalls of an approaching squadron of guards.\
 The only way to avoid confronting them is to go down the stairs. Do you [stay and fight] or [go down the stairs]?\n")
    if first_combat_query=="go down the stairs":
        print("Darwin would be proud.\n")
        decision_counter=0
    elif first_combat_query=="stay and fight":
        opponent=creatures.Creatures(name="hulking guard", hp=3, attack=6) #initializing creature. Might need to update if creatures updates.
        player.combat(opponent)
        decision_counter=2
    else:
        print(sass.sample_sass(), '\n')
    return(decision_counter)
    
