#!/usr/bin/env python3                                                                                     


#import modules                                                                                            
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles, wizard_encounter

from textFormat import input_s, print_s
from sass import sample_sass
from beer_encounter import beer_encounter
from attempt_climb import attempt_climb
from zookeeper_encounter import zookeeper_encounter
from brownie_encounter import brownie_encounter
from jared_encounter import shark_game
from easter_egg import easter_egg
from walk_in import walk_in

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
            input_s("As the daylight hits your face, you feel the warmth sink into your soul and your health points increase to " + str(player.hp) + ". You have a sudden flash of memory: the details are hazy, but you recall that you were imprisoned by a powerful wizard. Looking around you, you realize you are in a vaguely familiar courtyard - the courtyard of the wizard's castle! This is your chance to find the wizard and solve the mystery of your imprisonment - and take your revenge!\n", player)
            zookeeper_encounter(player)

            entry_query=input_s("You exit the menagerie and look around the courtyard. The outer wall is unscalable and the portcullis is down. There is a window two floors up the castle wall and a main entrance. Do you attempt to [climb] the wall or [walk] in the door?\n",player)
            while entry_query not in ["climb", "walk", "rope"]:
                entry_query=input_s(sample_sass(),player, "purple")
            if entry_query=="climb" or entry_query=="rope":
                success=attempt_climb(player, entry_query)
                if success==0:
                    print_s("You have fallen to your death.")
                    break
                elif success==1:
                    input_s("Light-footed as a prancercize instructor, you alight on the floor of a cozy room smelling of roses - what a relief after that sewer! You look around and see a sorceress perusing a perl manual at a nearby table.", player)
                    sorc_approach=input_s("Do you approach the sorceress?[yes] or [no]\n", player)
                    while sorc_approach not in ["yes", "no"]:
                        sorc_approach=input_s(sample_sass(),player, "purple")
                    if sorc_approach=="yes":
                        input_s("'Hello young traveler!' she sings.\n 'My name is Sofia. Sit with me and gain some perls of wisdom.'", player)
                        player.intelligence+=2
                        input_s("You spend a deeply enlightening hour with Sofia. As you rise from the table, she gives you this helpful hint: \n 'To defeat the wizard, gather all the intelligence you can'\n and she increases your intelligence score to " + str(player.intelligence) + ". You walk out of the room into a steamy spa.", player)
                        
                    elif sorc_approach=="no":
                        print_s("You walk past the sorceress and enter a steamy spa.\n")
                    
                    spa_query=input_s("There is a bubbling hottub in the spa. Do you sit in it?[yes] or [no]\n", player)
                    while spa_query not in ["yes", "no"]:
                        spa_query=input_s(sample_sass(),player, "purple")
                    if spa_query=="yes":
                        player.mana=3
                        input_s("You sit in the hottub and your mana is fully replenished to " + str(player.mana) + ".\n After your rejuvinating soak, you towel off and walk out the spa door and it locks behind you. Good thing you got dressed before walking out that door!", player)
                    elif spa_query=="no":
                        input_s("You walk right past the enticing hottub. Really?", player)
                    print_s("You exit into a sumptuously decorated hallway. Your feet sinking into the plush carpet, you notice a door cracked to your left.")
                elif success==2:
                    walk_in(player)
                    if player.hp<=0:
                        print_s("You made it so far...but this is how you die.")                
                        break
            elif entry_query=="walk":
                walk_in(player)
                if player.hp<=0:
                    print_s("You made it so far...but this is how you die.")                
                    break
            easter_query=input_s("Do you open the door? [yes] or [no]\n", player)
            while easter_query not in ["yes", "no"]:
                easter_query=input_s(sample_sass(), player, "purple")
            if easter_query=="yes":
                easter_egg(player)
            print_s("You come to the foot of a spiral staircase that circles upwards out of sight. Testing your physical fitness, you leap up eleven steps at a time. You slip through an archway and find yourself on a balcony.")
            shark_game(player)
            if player.hp<=0:
                print_s("Really? You lost to a drunken " + animal.name + "\n")
                break
            input_s("Slightly dazed from your latest encounter, you return to the spiral stairs and proceed cautiously upward. You look out of a window and realize you are approaching the top of the highest tower. Seeing the prison in the distance, your smoldering desire to confront the wizard bursts into flames.", player)
            wiz_puzzle=wizard_encounter.Wizard_encounter()
            wizard_result=wiz_puzzle.boss_battle(user=player)
            if wizard_result==True:
                input_s("You step through the door into a high-ceilinged room that looks very familiar. You approach an iMac and, your stomach fluttering, you enter the flash drive into the USB port.", player)
                input_s("A message appears on the screen:\n'Welcome back " + player.name + "! Upload memory?",player)
                input_s("And it all comes rushing back. You recall that fateful mistake - using your superuser powers to remove recursively the home directory of Simon and Sofia's cluster of servers. The years and years of data and code you somehow managed to delete from both local and remote repositories.", player)
                input_s("A final message prints on the screen:/n'Your permissions have been restored.'", player)
                input_s("Filled with gratitude, you return to your home as Baron(ess) of Hershey Manor, never to abuse sudo again.", player)
            else:
                print_s("Simon shakes his head in disappointment./n 'I can see you've learned nothing from this experience. I'm afraid there's only one place for sloppy coders in this universe.'")
                player.level=1
                
            player.level=3
        player.hp=0
    print_s("Game over", "red")
    play_again=input_s("Would you like to play again? [yes] or [no]")
    if play_again=="no":
        game_play=0
