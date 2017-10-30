#!/usr/bin/env python3


#import modules
import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles, mitchell_encounter, dice_encounter

from textFormat import input_s, print_s
from sass import sample_sass
from beer_encounter import beer_encounter

#initialize global variables
art = '''                                         
  @@@@@@@        @@@@@         @@@@@@@   
  @@@@@@@@      @@@@@@@        @@@@@@@@  
  @@!  @@@     @@!   @@@       @@!  @@@  
  !@!  @!@      !@  @!@        !@!  @!@  
  @!@@!@!        @!@!@         @!@@!@!   
  !!@!!!         !!!@  !!!     !!@!!!    
  !!:           !!:!!:!!:      !!:       
  :!:          :!:  !:!:       :!:       
   ::          ::: ::::::       ::       
   :            ::: :: :::      :  

           Prisons & Pythons      
 '''                                        

game_play=1
print(art)
print("Optimal Terminal window size = 100x75")
print("INSTRUCTIONS\n Actions are in [square brackets]\n Your various attacks are:\n [a]ttack which is the basic move,\n [r]isky which can have a bigger imapct but can miss the target\n or [m]agic always does max damage but the number of uses are limited\n If there is a wait, hit <enter>\n You can call up your [status] at any time  \n")
print("CREDITS\n ")
while game_play==1:# the player enters the loop. they cannot escape the loop until game_play is called not active.
    pre_query1=input("What's your name? ")
    pre_query2=input("How hard do you want this to be? [easy], [medium], or [hard] ")
    player=user.Prisoner(name=pre_query1, difficulty=pre_query2) 
    print_s("Your name is "+ player.name+", you have "+ str(player.hp)+ " health points. \n")
    read_statement=input_s("Press enter to begin.\n", player)
    
    levelone='''
        ..               _                          ..                                         
  x .d88"               u                     x .d88"                                          
   5888R               88Nu.   u.              5888R             u.      u.    u.              
   '888R        .u    '88888.o888c      .u     '888R       ...ue888b   x@88k u@88c.      .u    
    888R     ud8888.   ^8888  8888   ud8888.    888R       888R Y888r ^"8888""8888"   ud8888.  
    888R   :888'8888.   8888  8888 :888'8888.   888R       888R I888>   8888  888R  :888'8888. 
    888R   d888 '88%"   8888  8888 d888 '88%"   888R       888R I888>   8888  888R  d888 '88%" 
    888R   8888.+"      8888  8888 8888.+"      888R       888R I888>   8888  888R  8888.+"    
    888R   8888L       .8888b.888P 8888L        888R      u8888cJ888    8888  888R  8888L      
   .888B . '8888c. .+   ^Y8888*""  '8888c. .+  .888B .     "*888*P"    "*88*" 8888" '8888c. .+ 
   ^*888%   "88888%       `Y"       "88888%    ^*888%        'Y"         ""   'Y"    "88888%   
     "%       "YP'                    "YP'       "%                                    "YP'    
                                                                                                                                                                                          
    '''
    print(levelone)

    fake_query=input_s("Your eyelids flutter open. You look up to see a dank, mossy ceiling and stone walls with one bleak, barred window. You sit up and look around. You see an open door in front you, candlelight flickering behind it. You stumble blearily to your feet and walk through the door.\n", player)
    
#game begins
    while player.hp>0:
        while player.level==1:
            #Level one
            decision_counter=1
            while decision_counter==1:
                first_query=input_s("You walk down the hallway and see a set of stairs leading down into the dark. Do you go down the stairs? [yes] or [no]\n ", player)
                if first_query=="no":
                    decision_counter=first_encounter.first_combat(player)
                elif first_query=="yes":
                    decision_counter=0
                else:
                    print_s(sample_sass(), color='purple')
            if player.hp<=0:
                print_s("Why did you try to fight that hulking guard, you plonker? You're so dead.\n")
                break
            else:
                if decision_counter==0:
                    print_s("\nYou start creeping down the stairs. Moving as quietly as you can, you peer through the darkness.\n")
                elif decision_counter==2:
                    print_s("Wow, you actually beat that hulking guard. Impressive! You take his fancy dagger.\n")
                    player.setAttack(5)
                    print_s("You continue down the corrider and slip through an open door into a dark room.\n")
            #Here you enter the sleeping guard scenario.
            decision_counter = 1
            while decision_counter == 1:
                second_query=input_s("As your eyes begin to adjust to the low lighting, you notice a single guard slouched in a drunken stupor against a nearby wall. Do you [wake him up] or [attempt to creep] past him?\n", player)
                if second_query == "attempt to creep":
                    decision_counter = second_encounter.second_combat(player)
                elif second_query == "wake him up":
                    opponent=creatures.SleepingGuard()
                    print(opponent.art())
                    player.combat(opponent)
                    decision_counter = 2
                else:
                    print_s(sample_sass(), color='purple')
            if player.hp<=0:
                print_s("Seriously? He was half asleep. You die in shame.\n")
                break
            else:
                 if decision_counter==0:
                    print_s("Being careful to step around the guard, you quietly look around the room.\n")
                 elif decision_counter==2:
                    player.setAttack(2)
                    input_s("With an astounding display of physical prowess, you destroyed that sleepy guard. You take their pocket knife. \n", player)
                #you move forward and find a new room with a cask of whiskey hiding a trapdoor
                 beer_query=input_s("You notice a trapdoor under a wooden cask in the corner. Looks like there's still some sorghum whiskey in it. Do you drink the whiskey? [yes] or [no]\n", player)
                 while str(beer_query) not in ["yes", "no"]:
                    beer_query=input_s(sample_sass(), player, color='purple')
                 if beer_query=="yes":
                    beer_encounter(player)
                    if player.hp<=0:
                        break
                 elif beer_query=="no":
                    input_s("\nYou heave the cask into the corner exposing the trapdoor underneath.\n", player)
                 print_s("\nYou attempt to open the trapdoor, but you find that it is locked. But you seem to have awakened something within.\n")
                 fake_query=input_s("", player)
                 print_s("The trapdoor creaks open.\n")
                 fake_query=input_s("", player)
                 puzzle_query=input_s("You hear an eerie voice coming out of the dark depths.\n 'There is a way out through my sewer,\n but only the intellectually astute are permitted to enter.'\n The head and torso of boratK rise out of the darkness.\n", player)
                 my_puzzle=puzzles.Puzzles()
                 puzzle_success=my_puzzle.do_puzzle(user=player)
               

                 if puzzle_success==True:
                    print_s("BoratK sinks slowly back into the darkness, leaving the trapdoor open behind him. You cautiously descend into the depths below.\n\n")
                 else:
                    print_s("BoratK slams the trapdoor closed at your feet.\n")
                    fake_query=input_s("", player)
                    input_s("You hear the sound of an approaching creature coming down the stairs. You look desperately around the room and see there is no escape except through the locked trapdoor. You prepare to fight whatever is about to come down the stairs. Are you ready?\n", player)
                    print_s("This beast doesn't care if you're ready or not, it's coming.\n")
                    fake_query=input_s("", player)
                    opponent=creatures.Random()
                    print(opponent.art())
                    print_s("A vicious " + opponent.name + " leaps down the stairs and attacks!\n")
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
            fake_query=input_s("", player)
            print_s("You continue down this dark, dank tunnel ignoring the fact you're wading knee deep through a prison sewer, you're pretty gross!\nYou can hear something splashing in the water, and can hear demented giggling in the darkness...\n")
            fake_query=input_s("", player)
            print_s("With the little light avaliable at the end of the tunnel you spot some freak dressed as a funky ass clown emerging from behind a shopping trolley full of rope and trash\n")
            fake_query=input_s("", player)
            print_s("Without saying a word the clown throws some dice against the wall... it bekons at you and points at the dice...\n")
            
            dice_querey = input_s("You wonder if this pennywise wannabe is packing some heat and will finish you off right here, right now, if you don't entertain it. Do you want to [roll] the dice and see what happens, or bust past him and make a [run] for it\n", player)
            while str(dice_querey) not in ["roll","run"]:
                dice_querey=input_s(sample_sass(), player, color='purple')
            if dice_querey == "roll":
                dice_encounter.dice_game(player)
                fake_query=input_s("", player)           
            elif dice_querey == "run":
                print_s("You push that son of a gun face down into the hotdog flavoured water and run for you life before it gets up.\n")
                fake_query=input_s("", player)
            
            print_s("You sigh heavily after that encounter, and wonder what the hell just happened. You continue down the tunnel wondering how you got into ths situation... What's that? you hear another unusual noise further ahead. Its a gutteral hiss that could only be one thing!\n")
            fake_query=input_s("", player)
            
            print_s("There is a huge python blocking your $PATH,\n it lunges at you, pinning you in a corner, you have to fight!\n What is your first move?\n\n")
            decision_counter=1
            opponent = creatures.Python()
            print(opponent.art())
            player.combat(opponent)
            if player.hp<=0:
                print_s("Sweet lord Monty is one tough python!\n")
                break
            elif decision_counter==2:
                print_s("Hell yeeeah! I nailed that mofo. Maybe I was some bad ass Navy Seal or part of the SAS?\n")
                player.setAttack(2)
            fake_query=input_s("", player)
            print_s("Battered and bruised you slowly walk away from the twisted, bloody pile of python. You continue further into the tunnel and come to a bend, as you turn the corner you can see daylight shining brightly at the end.\n")
            player.hp+=20
            player.hpmax+=20
            #level two
            art2= '''
        ..               _                          ..         s                                   
  x .d88"               u                     x .d88"         :8      x=~                          
   5888R               88Nu.   u.              5888R         .88     88x.   .e.   .e.         u.   
   '888R        .u    '88888.o888c      .u     '888R        :888ooo '8888X.x888:.x888   ...ue888b  
    888R     ud8888.   ^8888  8888   ud8888.    888R      -*8888888  `8888  888X '888k  888R Y888r 
    888R   :888'8888.   8888  8888 :888'8888.   888R        8888      X888  888X  888X  888R I888> 
    888R   d888 '88%"   8888  8888 d888 '88%"   888R        8888      X888  888X  888X  888R I888> 
    888R   8888.+"      8888  8888 8888.+"      888R        8888      X888  888X  888X  888R I888> 
    888R   8888L       .8888b.888P 8888L        888R       .8888Lu=  .X888  888X. 888~ u8888cJ888  
   .888B . '8888c. .+   ^Y8888*""  '8888c. .+  .888B .     ^%888*    `'88%``"*888Y"     "*888*P"   
   ^*888%   "88888%       `Y"       "88888%    ^*888%        'Y"       `~     `"          'Y"      
     "%       "YP'                    "YP'       "%                                                
                                                                                                   
                                                                                                                                                                                                     
'''
            print(art2)   
            #print(status)


    gameover='''

        ....        .                                                         ....            _                                 
     .x88" `^x~  xH(`                                                     .x~X88888Hx.       u                                  
    X888   x8 ` 8888h                  ..    .     :                     H8X 888888888h.    88Nu.   u.                .u    .   
   88888  888.  %8888         u      .888: x888  x888.       .u         8888:`*888888888:  '88888.o888c      .u     .d88B :@8c  
  <8888X X8888   X8?       us888u.  ~`8888~'888X`?888f`   ud8888.       88888:        `%8   ^8888  8888   ud8888.  ="8888f8888r 
  X8888> 488888>"8888x  .@88 "8888"   X888  888X '888>  :888'8888.    . `88888          ?>   8888  8888 :888'8888.   4888>'88"  
  X8888>  888888 '8888L 9888  9888    X888  888X '888>  d888 '88%"    `. ?888%           X   8888  8888 d888 '88%"   4888> '    
  ?8888X   ?8888>'8888X 9888  9888    X888  888X '888>  8888.+"         ~*??.            >   8888  8888 8888.+"      4888>      
   8888X h  8888 '8888~ 9888  9888    X888  888X '888>  8888L          .x88888h.        <   .8888b.888P 8888L       .d888L .+   
    ?888  -:8*"  <888"  9888  9888   "*88%""*88" '888!` '8888c. .+    :"""8888888x..  .x     ^Y8888*""  '8888c. .+  ^"8888*"    
     `*88.      :88%    "888*""888"    `~    "    `"`    "88888%      `    `*888888888"        `Y"       "88888%       "Y"      
        ^"~====""`       ^Y"   ^Y'                         "YP'               ""***""                      "YP'                 
                                                                                                                                
    '''
    print(gameover)#print_s when you escape the second while loop.
    game_play=0 #gets you out of the outermost while loop.






    

