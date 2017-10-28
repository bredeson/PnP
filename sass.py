#!/usr/bin/env python3

import random

def sample_sass():
    sassy_retorts=["You've entered an invalid response, you sassy dog.", "Stop avoiding decisions.", "Don't you backtalk me.", "Use a keyboard much?"]
    index=random.randrange(len(sassy_retorts))
    return(sassy_retorts[index])

#sassy_retorts=["You've entered an invalid response, you sassy dog.", "Stop avoiding decisions.", "Don't you backtalk me."]

#sassy_retort=sample_sass(sassy_retorts)

#print(sassy_retort)
