#import random
#coin = random.choice(["heads", "tails"]) #indicate [] list

from random import choice #now we don't need to specify

coin = choice(["heads", "tails"])
print(coin)