#!/usr/bin/env python3

import creatures

def first_combat(player):
    first_combat_query=input("You enter a dark room. As you walk through, you step in a puddle. Crimson blood drips from your boot. .\
 You see a dead guard torn apart. Do you [search his body] or say a prayer and [keep moving]?\n")
    if first_combat_query=="search his body":
        print("You find a vial filled with a mysterious liquid.\n")
	
        decision_counter=0
    elif first_combat_query=="keep moving":
        print("You continue onward, pushing the thought of death out of your mind"
        decision_counter=2
    else:
        print(sass.sample_sass(), '\n')
    return(decision_counter)
    
