#!/usr/bin/env python3


#import modules
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles, mitchell_encounter, textFormat

from input_w_stats import input_s
from sass import sample_sass
from beer_encounter import beer_encounter

#initialize global variables

game_play=1

while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    print_s_s("Your name is ", player.name,", you have ", player.hp, " health points. \n", sep='')
    print_s_s("INSTRUCTIONS \n")
    read_statement=input_s("Press enter to begin.\n", player)

    fake_query=input_s("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone walls with one bleak, barred window. You sit up and look around. You see an open door in front you, candlelight flickering behind it. You stumble blearily to your feet and walk through the door.\n", player)
    
#game begins
    while player.hp>0:
        while player.level==1:
            decision_counter=1
            while decision_counter==1:
                first_query=input_s("You walk down the hallway and see a set of stairs leading down into the dark. Do you go down the stairs, [yes] or [no]?\n ", player)
                if first_query=="no":
                    decision_counter=first_encounter.first_combat(player)
                elif first_query=="yes":
                    decision_counter=0
                else:
                    print_s(sample_sass(), '\n')
            if player.hp<=0:
                print_s("Why did you try to fight that hulking guard, you plonker? You're so dead.\n")
                break
            else:
                if decision_counter==0:
                    print_s("You start creeping down the stairs. Moving as quietly as you can, you peer through the darkness.\n")
                elif decision_counter==2:
                    print_s("Wow, you actually beat that hulking guard. Impressive! You take his fancy dagger.\n")
                    player.setAttack(5)
                    print_s("You continue down the corrider and slip through an open door into a dark room.\n")
            #Here you enter the sleeping guard scenario.
            decision_counter=1
            while decision_counter==1:
                second_query=input_s("As your eyes begin to adjust to the low lighting, you notice a single guard slouched in a drunken stupor against a nearby wall. Do you [wake him up] or [attempt to creep] past him?\n", player)
                if second_query=="attempt to creep":
                    decision_counter=second_encounter.second_combat(player)
                elif second_query=="wake him up":
                    opponent=creatures.Creatures(name='sleepy guard', hp=10, attack=4)
                    player.combat(opponent)
                    decision_counter=2
                else:
                    print_s(sample_sass())
            if player.hp<=0:
                print_s("Seriously? He was half asleep. You die in shame.\n")
                break
            else:
                 if decision_counter==0:
                    print_s("Being careful to step around the guard, you quietly look around the room.\n")
                 elif decision_counter==2:
                    print_s("With an astounding display of physical prowess, you destroyed that sleepy guard. You take their pocket knife. \n")
                    player.setAttack(2)
            #you move forward and find a new room with a cask of whiskey hiding a trapdoor
                 beer_query=input_s("You notice a trapdoor under a wooden cask in the corner. Looks like there's still some sorghum whiskey in it. Do you drink the whiskey? [yes] or [no]\n", player)
                 while str(beer_query) not in ["yes", "no"]:
                    beer_query=input_s(sample_sass(), player)
                 if beer_query=="yes":
                    beer_encounter(player)
                    if player.hp<=0:
                        break
                 elif beer_query=="no":
                    input_s("You heave the cask into the corner exposing the trapdoor underneath.\n", player)
                 print_s("You attempt to open the trapdoor, but you find that it is locked. But you seem to have awakened something within.\n")
                 fake_query=input_s("", player)
                 print_s("The trapdoor creaks open.\n")
                 fake_query=input_s("", player)
                 puzzle_query=input_s("You hear an eerie voice coming out of the dark depths.\n 'There is a way out through my sewer, but only the intellectually astute are permitted to enter.'\n The head and torso of boratK rise out of the darkness.\n", player)
                 my_puzzle=puzzles.Puzzles()
                 puzzle_success=my_puzzle.do_puzzle(user=player)
               

                 if puzzle_success==True:
                    print_s("BoratK sinks slowly back into the darkness, leaving the trapdoor open behind him. You cautiously descend into the depths below.\n")
                 else:
                    print_s("BoratK slams the trapdoor closed at your feet.\n")
                    fake_query=input_s("", player)
                    input_s("You hear the sound of an approaching creature coming down the stairs. You look desperately around the room and see there is no escape except through the locked trapdoor. You prepare to fight whatever is about to come down the stairs. Are you ready?\n", player)
                    print_s("This beast doesn't care if you're ready or not, it's coming.\n")
                    fake_query=input_s("", player)
                    opponent=creatures.Random()
                    print_s("A vicious", opponent.name, "leaps down the stairs and attacks!\n")
                    fake_query=input_s("", player)
                    player.combat(opponent)
                    if player.hp<=0:
                        print_s("So this is how it ends.\n")
                        break
                    else:
                        print_s("Slumping over the corpse of the defeated " + opponent.name + ", you notice a tiny golden key. Summoning all the strength you have left after that epic battle, you grab the key and hobble over to the trapdoor... \n")
                        fake_query=input_s("", player)
                        print_s("To your relief the key fits the lock and the trapdoor opens with a little effort and you cautiously descend into the depths below.\n") 
            
            mitchell_encounter.oyster_encounter(player)



    print_s("Game Over.")#print_s when you escape the second while loop.
    game_play=0 #gets you out of the outermost while loop.






    

