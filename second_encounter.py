#!/usr/bin/env python3

import creatures, random

art = '''
                z 
                         z 
                          Z 
                .--.  Z Z 
               / _(c\   .-.     __  
              | / /  '-;   \--'`  `\______ 
              \_\/'/ __/ )  /  )   |      \--, 
              | \`""`__-/ .'--/   /--------\  \ 
               \`\  ///-\/   /   /---;-.    '-' 
                            (________\  \ 
                                      '-' 
'''


def second_combat(player):

    print(art)
        
    d_10 = random.randint(1,10)
    

    if d_10 > 2:
        print("Sneaky sneaky... you did it.\n")
        decision_counter=0
    
    elif d_10 <= 2:
        print("Oh snap, you woke him up you club footed moose. \n")
        opponent=creatures.Creatures(name="sleepy guard", hp=12, attack=4) #initializing creature. Might need to update if creatures updates.
        player.combat(opponent)
        decision_counter=2
    
    return(decision_counter)
