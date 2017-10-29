#!/usr/bin/env python3

import random

def sample_sass():
    sassy_retorts=["You've entered an invalid response, you sassy dog.", "Stop avoiding decisions.", "Don't you backtalk me.", "Use a keyboard much?", "That's not an option, you scurvy cur!", "Maybe you need glasses. Try that again.", "Keep going like this and you'll never get into prison."]
    index=random.randrange(len(sassy_retorts))
    return(sassy_retorts[index]+'\n')

#sassy_retorts=["You've entered an invalid response, you sassy dog.", "Stop avoiding decisions.", "Don't you backtalk me."]

#sassy_retort=sample_sass(sassy_retorts)

#print(sassy_retort)
