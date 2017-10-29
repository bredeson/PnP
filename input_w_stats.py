#!/usr/bin/env python3

def input_s(text, user):
    query=input(text)
    while query=="status":
        print("\nName:{}\nhp:{}\ndifficulty:{}\nattack:{}\n".format(user.name, user.hp, user.difficulty, user.attack))
        query=input(text)
    return(query)
