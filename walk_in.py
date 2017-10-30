#!/usr/env/bin python3

import user, os, sass, first_encounter, random, time, creatures, second_encounter, puzzles, wizard_encounter

from textFormat import input_s, print_s
from sass import sample_sass
from beer_encounter import beer_encounter
from attempt_climb import attempt_climb
from zookeeper_encounter import zookeeper_encounter
from brownie_encounter import brownie_encounter
from jared_encounter import shark_game
from easter_egg import easter_egg


def walk_in(player):
    opponent=creatures.Magic()
    print_s("You strut confidently through the main castle door. You enter an impressively portioned entranc\
e hall lit by sunlight streaming through the tall mullioned windows. You briefly admire the marble statues and tapestrie\
s lining the walls.")
    input_s("You see a " + opponent.name + " taking a fighting stance ten meters in front of you.", player)
    print(opponent.art())
    player.combat(opponent)
    if player.hp>0:
        player.mana+=1
        input_s("Bomb diggity. You emerge victorious from your latest escapade. Defeating this magical creature \
increases your mana to " + str(player.mana)+ ".\n", player)
        print_s("At the end of the entrance hall is a magnificent pair of staircases sweeping up to the next lev\
el. ")
        stair_query=input_s("Do you go up the stairs?[yes] or [no]\n", player)
        while stair_query not in ["yes", "no"]:
            stair_query=input_s(sample_sass(), player, "purple")
        if stair_query=="no":
            while(stair_query=="no"):
                passive_actions=["A breeze blows gently through the windows.", "You hear the sound of birds chir\
ping outside.", "A mouse scurrying along the wall rustles gently.", "You check your watch.", "All remains quiet in the e\
ntrance hall.", "You think about how long it must take to chisel a sculpture.", "You watch an ant crawl by on the floor.\
", "You contemplate what your life could have been if you hadn't gone to prison.", "You spy a new oil painting on an eas\
el and watch it dry. " ]
                index=random.randrange(len(passive_actions))
                print_s(passive_actions[index])
                time.sleep(5)
                stair_query=input_s("Do you go up the staircase yet?[yes] or [no]\n", player)
            brownie_encounter(player)
            input_s("At the top of the stairs you enter a sumptuously decorated hallway. The thick carpet muffles th\
e sound of your footsteps. You pass several creepy old paintings and notice a door cracked to your left.", player)
