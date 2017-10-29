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
    decision = input_s("[Blood] or [Knowledge]?", player, color="red")
    
    while str(decision) not in ["Blood", "Knowledge"]:
      decision=input_s(sass.sample_sass(), player)

    if decision=="Blood":  
      if d_10 > 4:
          print_s("Wow, all those years playing street dice in the ghetto paid off, you gain +2 health points\n")
          print_s("Well played my friend here take this [rope], I'm certain it'll come in handy\n", color="red")
          player.hp+=2
    
      elif d_10 <= 4:
          print_s("Shoot... you suck at this, the clown slaps you upside the head. You loose 1 health point\n the clown slopes off behind his trolley and leaves the way clear\n")
          player.hp-=1
    
    elif decision=="Knowledge":
      if d_10 > 4:
          print_s("Wow, all those years playing street dice in the ghetto paid off, you gain +2 intelligence \n")
          print_s("Well played my friend here take this [rope], I'm certain it'll come in handy\n", color="red")
          player.intelligence+=2
    
      elif d_10 <= 4:
          print_s("Shoot... you suck at this, the clown laughs in your face. You loose 1 intelligence point\n the clown slopes off behind his trolley and leaves the way clear\n")
          player.intelligence-=1
