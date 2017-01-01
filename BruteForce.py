from RandomSetGenerator import randomSet
from createCSV import write, write2, write3
from random import randint
import timeit
import random
import numpy

BITLENGTH = 1023
N = 1
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


def exhaustive():
    averagearray = []
    for k in range(N, N+1):
        print k
        y = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            subsetsum(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            y.append(elapsed)
        avg = sum(y) / float(len(y))
        averagearray.append(avg)
    write("AverageBF" + '-' + str(BITLENGTH) + '-' + str(N), averagearray)


def subset_sum(A, target):
    ways = [0] * (target + 1)
    ways[0] = 1
    ways_next = ways[:]
    for x in A:
        for j in range(x, target + 1):
            ways_next[j] += ways[j - x]
        ways = ways_next[:]
    return ways[target]


def dynprog():
    averagearray = []
    for k in range(N, N+1):
        y = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            subset_sum(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            y.append(elapsed)
        avg = sum(y) / float(len(y))
        averagearray.append(avg)
    write("Averagedyn" + '-' + str(BITLENGTH) + '-' + str(N), averagearray)


def greedy(array, value):
    sum = 0
    elements = []
    array2 = sorted(array[:])
    for i in reversed(array2):
        if sum + i <= value:
            sum = sum + i
            elements.append(i)
            array2.remove(i)
        else:
            pass
    return sum, value


def greedystart():
    for k in range(1, 501):
        arrayofpercent = []
        for i in range(1000):
            testset = randomSet(k)
            gotten, value = greedy(testset, random.randint(0, BITLENGTH))
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write3("AverageGreedy" + '-' + str(BITLENGTH) + '-' + str(N), arrayofpercent, k)

def grasp(array, target):
    #Break set into several subsets or 'neighbourhoods', search random neighbourhood and it's neighbours for highest number
    #If higher number found, search their neighbours too. If no improvement is found, jump to random neighborhood again and repeat until finished.
    sum = 0
    elements = []
    while ((sum < target) & (len(array) >= 3)):
        optimisedChoice = optimisedSearch(array, target, sum)
        if min(array) >= target | (optimisedChoice == 0 & len(array) == 3):
            return 0, target
        elif sum + array[optimisedChoice] <= target:
            sum = sum + array[optimisedChoice]
            elements.append(array[optimisedChoice])
            array.pop(optimisedChoice)
    return sum, target

def optimisedSearch(array, target, sum):
    #print str(len(array))
    neighbourhood = randint(1, len(array) - 2)
    bottomNeighbour = array[neighbourhood - 1]
    middleNeighbour = array[neighbourhood]
    topNeighbour = array[neighbourhood + 1]

    neighbourhoodToFilter = {neighbourhood - 1 : bottomNeighbour, neighbourhood : middleNeighbour, neighbourhood + 1 : topNeighbour}

    if max(neighbourhoodToFilter, key=neighbourhoodToFilter.get) + sum <= target:
        return max(neighbourhoodToFilter, key=neighbourhoodToFilter.get)
    elif numpy.median(neighbourhoodToFilter, key=neighbourhoodToFilter.get) + sum <= target:
        return numpy.median(neighbourhoodToFilter, key=neighbourhoodToFilter.get)
    elif min(neighbourhoodToFilter, key=neighbourhoodToFilter.get) + sum <= target:
        return min(neighbourhoodToFilter, key=neighbourhoodToFilter.get)

    return 0

def graspStart():
    for k in range(1, 501):
        percentageAccuracy = []
        for i in range(1):
            testSet = randomSet(k)
            gotten, value = grasp(testSet, random.randint(0,BITLENGTH))
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            percentageAccuracy.append(percent)
        write3("AverageGRASP" + '-' + str(BITLENGTH) + '-' + str(N), percentageAccuracy, k)




def simulatedAnnealing(array, value, loops):
    best = 0
    for t in range(loops):
        sum = 0
        testarray = array[:]
        for i in range(len(array)):
            randomnum = random.randint(0, len(testarray)-1)
            if sum + testarray[randomnum] <= value:
                sum += testarray[randomnum]
                testarray.pop(randomnum)
            if sum == value:
                return sum, value
            if sum > best:
                best = sum
    return best, value


def runsimulatedAnnealing():
    arrayofpercent = []
    for k in range(1, N):
        print k
        for i in range(1000):
            testset = randomSet(20)
            # N, set size = 20
            gotten, value = simulatedAnnealing(randomSet(20), random.randint(0, BITLENGTH), k)
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write2("simulatedAnnealing"+str(BITLENGTH)+str(k), arrayofpercent, k)


BITLENGTH = BITLENGTH#*2+1
graspStart()
