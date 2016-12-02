from RandomSetGenerator import randomSet
from createCSV import write
import timeit
import random

BITLENGTH = 1023
N = 22
# numbers of sets +1


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


def subset_sum(A, target):
    ways = [0] * (target + 1)
    ways[0] = 1
    ways_next = ways[:]
    for x in A:
        for j in range(x, target + 1):
            ways_next[j] += ways[j - x]
        ways = ways_next[:]
    return ways[target]


def subsetproblem():
    averagearray = []
    for k in range(1, N):
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


def dynprog():
    averagearray = []
    for k in range(1, N):
        y = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            subset_sum(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            y.append(elapsed)
        avg = sum(y) / float(len(y))
        averagearray.append(avg)
    write("Averagedyn", averagearray)


def greedy(array, value):
    sum = 0
    elements = []
    array = sorted(array)
    for i in reversed(array):
        if sum + i <= value:
            sum = sum + i
            print sum
            elements.append(i)
        else:
            pass
    return sum, elements


def greedystart():
    averagearray = []
    for k in range(1, N):
        y = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            greedy(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            y.append(elapsed)
        avg = sum(y) / float(len(y))
        averagearray.append(avg)
    write("AverageGreedy", averagearray)

greedystart()
