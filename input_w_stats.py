#!/usr/bin/env python3

def input_s(text, user):
    query=input(text)
    while query=="status":
        print("\nName\thp\tdifficulty")
        print("{}\t{}\t{}\n".format(user.name, user.hp, user.difficulty))
        query=input(text)
    return(query)
