#!/usr/bin/env python3                                                                                     


#import modules                                                                                            
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles

from textFormat import input_s, print_s
from sass import sample_sass
from beer_encounter import beer_encounter
from attempt_climb import attempt_climb

#initialize global variables                                                                               

game_play=1

while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is changed

    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2, level=2)
    print("Your name is ", player.name,", you have ", player.hp, " health points. \n", sep='')
    read_statement=input_s("Press enter to begin.\n", player)

#game begins                                                                                               
    while player.hp>0:
        while player.level==2:
            print_s("As the daylight hits your face, you have a sudden flash of memory. The details are hazy, but you recall that you were imprisoned by a powerful wizard. Looking around you, you realize you are in a vaguely familiar courtyard - the courtyard of the wizard's castle! The outer wall is unscalable and the portcullis is up. This is your chance to find the wizard and solve the mystery of your imprisonment - and take your revenge!\n")
            time.sleep(3)
            entry_query=input_s("There is a window two floors up the castle wall and a main entrance. Do you [attempt the climb] or [enter the door]?\n",player)
            while entry_query not in ["attempt the climb", "enter the door", "rope"]:
                entry_query=input_s(sample_sass(),player)
            if entry_query=="attempt the climb" or "rope":
                success=attempt_climb(player, entry_query)
                if success==0:
                    print_s("You have fallen to your death.")
                    break
                elif success==1:
                    print_s("You are in the spa.")
            elif entry_query=="enter the door":
                print("you go in the door")
            print_s("You made it out of the ifs")
            player.level=3
        player.hp=0
    print_s("Game over", "red")
    game_play=0
