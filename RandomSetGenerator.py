import random

def randomSet(elements):
    randomNumbers = random.sample(range(0,1024),elements)
    return randomNumbers

print randomSet(5)
