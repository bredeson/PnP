#!/usr/bin/env python3


#import modules
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles


#initialize global variables

game_play=1

while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    print("Your name is ", player.name,", you have ", player.hp, " health points. \n", sep='')
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
            else:
                if decision_counter==0:
                    print("You start creeping down the stairs. Moving as quietly as you can, you peer through the darkness.\n")
                elif decision_counter==2:
                    print("Wow, you actually beat that hulking guard. Impressive! You take his fancy dagger.\n")
                    player.setAttack(5)
                    print("You continue down the corrider and slip through an open door into a dark room.\n")
            #Here you enter the sleeping guard scenario.
            decision_counter=1
            while decision_counter==1:
                second_query=input("As your eyes begin to adjust to the low lighting, you notice a single guard slouched in a drunken stupor against a nearby wall. Do you [wake him up] or [attempt to creep] past him?\n")
                if second_query=="attempt to creep":
                    decision_counter=second_encounter.second_combat(player)
                elif second_query=="wake him up":
                    opponent=creatures.Creatures(name='sleepy guard', hp=10, attack=4)
                    player.combat(opponent)
                    decision_counter=2
                else:
                    print(sass.sample_sass(), '\n')
            if player.hp<=0:
                print("Seriously? He was half asleep. You die in shame.")
                break
            else:
                 if decision_counter==0:
                    print("Being careful to step around the guard, you quietly look around the room.")
                 elif decision_counter==2:
                    print("With an astounding display of physical prowess, you destroyed that sleepy guard. You take their pocket knife. \n")
                    player.setAttack(2)
                 beer_query=input("You notice a trapdoor under a wooden keg in the corner. Looks like there's still some beer in it. Do you drink the beer? [yes] or [no]\n")
                 while str(beer_query) not in ["yes", "no"]:
                    beer_query=input(sass.sample_sass(), '\n')
                 if beer_query=="yes":
                    player.attack-=2
                    input("You empty the remains of the keg. Not the best beer you've ever had. The loss of coordination reduces your attack ability to " + str(player.attack) + ". You toss the empty keg to one side and expose the trapdoor.")
                 elif beer_query=="no":
                    input("You heave the keg into the corner exposing the trapdoor underneath.")
                 puzzle_query=input("You pull the trapdoor open. You hear an eerie voice coming out of it's dark depths.\n 'There is a way out through my sewer, but only the intellectually astute are permitted to enter.'\n The head and torso of boratK rise out of the darkness.\n")
                 my_puzzle=puzzles.Puzzles()
                 puzzle_success=my_puzzle.do_puzzle()
                #puzzle_success=False

                 if puzzle_success==True:
                    print("BoratK sinks slowly back into the darkness, leaving the trapdoor open behind him. You cautiously descend into the depths below.\n")
                 else:
                    print("BoratK slams the trapdoor closed at your feet.\n")
                    time.sleep(5)
#Come back tomorrow and make this a modeule of it's own
                    input("You hear the sound of an approaching creature coming down the stairs. You look desperately around the room and see there is no escape except through the locked trapdoor. You prepare to fight whatever is about to come down the stairs. Are you ready?")
                    print("This beast doesn't care if you're ready or not, it's coming.")
                    opponent=creatures.Random()
                    print("A vicious", opponent.name, "leaps down the stairs and attacks!")
                    player.combat(opponent)

                #you will soon have an oyster encounter

    print("Game Over.")#print when you escape the second while loop.
    game_play=0 #gets you out of the outermost while loop.






    

