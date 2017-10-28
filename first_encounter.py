#!/usr/bin/env python3

def first_combat():
    first_combat_query=input("You hear the heavy footfalls of an approaching squadron of guards.\
 The only way to avoid confronting them is to go down the stairs. Do you [stay] or [go down the stairs]?\n")
    if first_combat_query=="go down the stairs":
        print("Darwin would be proud.\n")
    elif first_combat_query=="stay":
        print("you fight the guards.\n")
    else:
        print(sass.sample_sass(), '\n')

    
