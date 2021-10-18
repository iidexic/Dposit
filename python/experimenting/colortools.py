import random as rng

def randcolor(): # Function gives random color

    nowcolor = (rng.randint(0,255),rng.randint(0,255),rng.randint(0,255))
    return nowcolor

def randdirection():
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    return directions[rng.randint(0,3)]

    