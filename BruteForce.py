from RandomSetGenerator import randomSet
from createCSV import write
import timeit
import random

BITLENGTH = 1023


def subsetsum(inputArray, targetNum):
    if len(inputArray) == 0:
        return None
    else:
        if inputArray[0] == targetNum:
            return [inputArray[0]]
        else:
            subset = subsetsum(inputArray[1:], (targetNum - inputArray[0]))
            if subset:
                return [inputArray[0]] + subset
            else:
                return subsetsum(inputArray[1:], targetNum)

def subsetproblem():
    averagearray = []
    for k in range(1, 26):
        y = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            subsetsum(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            y.append(elapsed)
        avg = sum(y) / float(len(y))
        averagearray.append(avg)
    write("Average", averagearray)
