from RandomSetGenerator import randomSet
from createCSV import write, write2, write3, write4
from random import randint
import timeit
import random
import numpy

BITLENGTH = 33000
N = 101


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
    for k in range(N, N + 1):
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
    for k in range(N, N + 1):
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


def grasp(array, target):
    # Break set into several subsets or 'neighbourhoods', search random neighbourhood and it's neighbours for highest number
    # If higher number found, search their neighbours too. If no improvement is found, jump to random neighborhood again and repeat until finished.
    sum = 0
    elements = []
    while ((sum < target) & (len(array) >= 3)):
        optimisedChoice = optimisedSearch(array, target, sum)
        print optimisedChoice
        # print "array",array,"target",target,"sum",sum,"optimised",array[optimisedChoice]
        if min(array) >= target | (optimisedChoice == 0 & len(array) == 3):
            return sum, target
        elif sum + array[optimisedChoice] <= target:
            sum = sum + array[optimisedChoice]
            print "elif, new sum =", sum
            elements.append(array[optimisedChoice])
            array.pop(optimisedChoice)
    return sum, target


def optimisedSearch(array, target, sum):
    neighbourhood = randint(1, len(array) - 2)
    bottomNeighbour = array[neighbourhood - 1]
    middleNeighbour = array[neighbourhood]
    topNeighbour = array[neighbourhood + 1]

    neighbourhoodToFilter = {neighbourhood - 1: bottomNeighbour, neighbourhood: middleNeighbour,
                             neighbourhood + 1: topNeighbour}

    median = numpy.median(neighbourhoodToFilter.values())

    medianKey = [key for key, value in neighbourhoodToFilter.iteritems() if value == median][0]

    if array[max(neighbourhoodToFilter, key=neighbourhoodToFilter.get)] + sum <= target:
        return max(neighbourhoodToFilter, key=neighbourhoodToFilter.get)
    elif median + sum <= target:
        return medianKey
    elif array[min(neighbourhoodToFilter, key=neighbourhoodToFilter.get)] + sum <= target:
        return min(neighbourhoodToFilter, key=neighbourhoodToFilter.get)

    return 0


def graspStart():
    for k in range(1, 21):
        percentageAccuracy = []
        for i in range(50):
            testSet = randomSet(k)
            gotten, value = grasp(testSet, random.randint(0, BITLENGTH))
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
            randomnum = random.randint(0, len(testarray) - 1)
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
    arrayoftime = []
    for k in range(1, N):
        for i in range(1000):
            testset = randomSet(20)
            # N, set size = 20
            start_time = timeit.default_timer()
            gotten, value = simulatedAnnealing(randomSet(k), random.randint(0, BITLENGTH), k)
            elapsed = timeit.default_timer() - start_time
            arrayoftime.append(elapsed)
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write4("simulatedAnnealing", arrayofpercent, arrayoftime, k)


def greedystart():
    for k in range(1, 501):
        arrayofpercent = []
        arrayoftime = []
        for i in range(1000):
            testset = randomSet(k)
            start_time = timeit.default_timer()
            gotten, value, elements1231231, array123123123 = greedy(testset, random.randint(0, BITLENGTH))
            elapsed = timeit.default_timer() - start_time
            arrayoftime.append(elapsed)
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write4("AverageGreedy", arrayofpercent, arrayoftime, k)


def greedy(array, value):
    sum1 = 0
    elements = []
    array2 = sorted(array[:])
    for i in reversed(array2):
        if sum1 + i <= value:
            sum1 = sum1 + i
            elements.append(i)
            array2.remove(i)
        else:
            pass
    return sum1, value, elements, array2


def greedyrandom(array, value):
    sum1 = 0
    elements = []
    array2 = array[:]
    array3 = array2[:]
    while array2:
        randomvalue = randint(0, len(array2)-1)
        if (sum1+array2[randomvalue]) <= value:
            sum1 = sum1+array2[randomvalue]
            elements.append(array2[randomvalue])
            array3.pop(randomvalue)
        array2.pop(randomvalue)
    return sum1, value, elements, array3


def grasp():
    for k in range(1, 51):
        arrayofpercent = []
        arrayoftime = []
        for i in range(1000):
            start_time = timeit.default_timer()
            testset = randomSet(k)
            target1 = random.randint(0, (BITLENGTH))
            gotten, value, elements, spares = greedyrandom(testset, target1)
            bestsol, RCL = localSearch(elements, spares, target1)
            for x in range(20):
                bestsol, RCL = localSearch(bestsol, RCL, target1)
            elapsed = timeit.default_timer() - start_time
            arrayoftime.append(elapsed)
            try:
                percent = sum(bestsol) / float(target1) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write4("Grasp", arrayofpercent, arrayoftime, k)


def check(best, candidate, target):
    if candidate > target:
        return False
    if candidate > best:
        return True


def localSearch(best, setOfNumbers, target):
    backup = best[:]
    bestcase = sum(best)
    best.sort(reverse=True)
    setOfNumbers.sort(reverse=True)
    for place, value in enumerate(setOfNumbers):
        for place2, value2 in enumerate(best):
            besttest = best[:]
            besttest[place2] = value
            if check(bestcase, sum(besttest), target):
                setOfNumbers.pop(place)
                return besttest, setOfNumbers
    return backup, setOfNumbers


runsimulatedAnnealing()