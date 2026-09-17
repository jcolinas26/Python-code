#use an external library

import random #import random library to use it on our code

coin = random.choice(["heads", "tails"]) #use one of the functions of random to simulate a coin toss -> random.choice takes a list of elements and choose one of them randomly
print (coin)

#--------------
from random import choice #-> other way to do it, in this case, we import only the function choice, not everything random module has

coin = choice(["heads", "tails"]) 
print (coin)

#--------------

numbrer = random.randint(1,10) #radnint returns a random between the 2 values passed
print(numbrer)

#--------------

cards = ["queen", "jack", "king"]
random.shuffle(cards) #shuffle returns the same list but with its elements shuffled
for card in cards:
    print(card)