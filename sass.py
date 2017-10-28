#!/usr/bin/env python3

import random

def sample_sass(sass):
    index=random.randrange(len(sass))
    return(sass[index])

sassy_retorts=["You've entered an invalid response, you sassy dog.", "Stop avoiding decisions.", "Don't you backtalk me."]

sassy_retort=sample_sass(sassy_retorts)

print(sassy_retort)
