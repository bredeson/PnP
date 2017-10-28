#!/usr/bin/env python3


#import modules
import user, os

#initialize global variables

while game_play=='active':# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    

#game begins
    while player.hp>0:
        while player.escapeStatus==False:
            print("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone walls with one bleak, barred window. You sit up and look around. You see an open door in front you, candlelight flickering behind it. You stumble blearily to your feet and walk through the door. Do you go [left] or [right]?")
        #sample a location when we get to that
            first_query=input("You walk down the hallway and see a set of stairs leading down into the dark. Do you go down the stairs, [yes] or [no]? ")

            if first_query=="no":
                print("It's dark down here, too bad we don't have items enabled yet.")

            elif first_query=="yes":
                print("You creep down the stairs.")

            else:
                print("sass")

    print("Game Over.")#print when you escape the second while loop.
    game_play='not active' #gets you out of the outermost while loop.






    

