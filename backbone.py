#!/usr/bin/env python3


#import modules
import user, os, sass, first_encounter, random, time, creatures


#initialize global variables

game_play=1

while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    print("Your name is", player.name,", you have", player.hp, "health points. \n")
    read_statement=input("Press enter to begin.\n")

    fake_query=input("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone walls with one bleak, barred window. You sit up and look around. You see an open door in front you, candlelight flickering behind it. You stumble blearily to your feet and walk through the door.\n")
    
#game begins
    while player.hp>0:
        while player.escapeStatus==False:
            decision_counter=1
            while decision_counter==1:
                first_query=input("You walk down the hallway and see a set of stairs leading down into the dark. Do you go down the stairs, [yes] or [no]?\n ")
                if first_query=="no":
                    decision_counter=first_encounter.first_combat(player)
                elif first_query=="yes":
                    decision_counter=0
                else:
                    print(sass.sample_sass(), '\n')
            if player.hp<=0:
                print("Why did you try to fight that hulking guard, you plonker? You're so dead.")
                break
            if decision_counter==0:
                print("You start creeping down the stairs. Moving as quietly as you can, you peer through the darkness.\n")
            elif decision_counter==2:
                print("Wow, you actually beat that hulking guard. Impressive! You take his fancy dagger.")
                player.setAttack(5)
                print("You continue down the corrider and slip through an open door into a dark room.")

    print("Game Over.")#print when you escape the second while loop.
    game_play=0 #gets you out of the outermost while loop.






    

