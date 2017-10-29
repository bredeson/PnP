#!/usr/bin/env python3                                                                                     


#import modules                                                                                            
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles

from input_w_stats import input_s
from sass import sample_sass
from beer_encounter import beer_encounter

#initialize global variables                                                                               

game_play=1

while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is called not\
 active.                                                                                                   
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2, level=2)
    print("Your name is ", player.name,", you have ", player.hp, " health points. \n", sep='')
    read_statement=input_s("Press enter to begin.\n", player)

    fake_query=input_s("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone wall\
s with one bleak, barred window. You sit up and look around. You see an open door in front you, candleligh\
t flickering behind it. You stumble blearily to your feet and walk through the door.\n", player)

#game begins                                                                                               
    while player.hp>0:
        while player.level==2:
            print("this code is working")
            player.level==3
        player.hp==0
    print("Game over")
