#!/usr/bin/env python3

import random
from sass import sample_sass
from textFormat import input_s, print_s, input_ss

def attempt_climb(user, climb_query):
    success=0
    while user.hp>0 and success==0 and climb_query=="climb":
        success_rate=random.randrange(0,10)
        if success_rate<6:
            user.hp-=2
            climb_query=input_ss("You were unsuccessful scaling the wall and your health points are reduced to "+ str(user.hp) + ". Do you want to attempt the [climb] again or [walk] in the door?\n", secrets="rope", user=user)
        else:
            success=1
            print_s("You've successfully climbed through the window!")
    if user.hp<=0:
        print_s("You really should have tried the door.")
    elif climb_query=="rope":
        print_s("You deftly swing the rope over a gargoyle flanking the window and scamper up the wall like a white-faced capuchin.")
        success=1
    elif climb_query=="walk":
        success=2
    return(success)
    
            


