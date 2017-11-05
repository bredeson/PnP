#!/usr/bin/env python3

import sass
from textFormat import input_s, print_s

def beer_encounter(user):
    response_list=["You take a drink of sumptuous sorghum whiskey, the finest you've ever tasted.", "You drink some more, it's been quite a day after all.", "You feel at one with all of humanity, but you're also losing fine motor control.", "You're getting a little woozy. Are you sure this is a good idea?", "Your vision is starting to blur and it's hard to see the cask anymore.", "You can't stand.", "You go into a catatonic stupor. You aren't conscious for your death, but rest assured it was embarrassing."]
    drink_query="yes"
    extra_drinks=0
    while drink_query=="yes":
        print_s(response_list[extra_drinks])
        user.attack-=1
        if extra_drinks<6:
            print_s("Your attack ability has been reduced to "+ str(user.attack)+".")
        if extra_drinks%2==1:
            user.intelligence-=1
            print_s("Your intelligence has been reduced to " + str(user.intelligence)+".")
        if extra_drinks>1 and extra_drinks<6:
            user.hp-=1
            print("Your health points have been reduced to " + str(user.hp) + ".") 
        if extra_drinks>=6:
            user.hp=0
            break
        drink_query=input_s("Do you want to keep drinking?", user)
        extra_drinks+=1
        while drink_query not in ["yes","no"]:
            drink_query=input_s(sass.sample_sass(), user, "purple")
