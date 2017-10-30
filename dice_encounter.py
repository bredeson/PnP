#!/usr/bin/env python3

import creatures, random, sass, time
from textFormat import print_s, input_s

art = '''
       ,            _..._            ,
      {'.         .'     '.         .'}
     { ~ '.      _|=    __|_      .'  ~}
    { ~  ~ '-._ (___________) _.-'~  ~  }
   {~  ~  ~   ~.'           '. ~    ~    }
  {  ~   ~  ~ /   /\     /\   \   ~    ~  }
  {   ~   ~  /    __     __    \ ~   ~    }
   {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}
    { ~   ;(      \/ .-. \/      );   ~ }
     { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }
      '-._~ \   (`-._'-'_.-')   / ~_.-'
          '--\   `'._'"'_.'`   /--'
              \     \`-'/     /
               `\    '-'    /'
                 `\       /'
                   '-...-'

'''


def dice_game(player):

    print(art)
        
    d_10 = random.randint(1,10)

    print_s("You go to pick up the dice and the clown whispers...")
    time.sleep(2)
    decision = input_s("[Blood] or [Power]?\n", player, color="red")
    
    while str(decision) not in ["Blood", "Power"]:
      decision=input_s(sass.sample_sass(), player, color='purple')

    if decision=="Blood" or decision=="blood":  
      if d_10 > 4:
          print_s("\nWow, all those years playing street dice in the ghetto paid off, you gain +2 health points\n")
          print_s("\nWell played my friend here take this [rope], I'm certain it'll come in handy\n", color="red")
          player.hp+=2
    
      elif d_10 <= 4:
          print_s("\nShoot... you suck at this, the clown slaps you upside the head. You loose 1 health point\n the clown slopes off behind his trolley and leaves the way clear\n", color='purple')
          player.hp-=1
    
    elif decision=="Power" or decision=="power":
      if d_10 > 4:
          print_s("\nWow, all those years playing street dice in the ghetto paid off, you gain +2 attack \n")
          print_s("\nWell played my friend here take this [rope], I'm certain it'll come in handy\n", color="red")
          player.attack+=2
    
      elif d_10 <= 4:
          print_s("\nShoot... you suck at this, the clown laughs in your face. You loose 1 attack point\n the clown slopes off behind his trolley and leaves the way clear\n", color='purple')
          player.attack-=1
