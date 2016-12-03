from RandomSetGenerator import randomSet
from createCSV import write, write2
import timeit
import random

BITLENGTH = 1023
N = 20
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
    write("AverageBF" + str(BITLENGTH) + str(N), averagearray)


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
    write("Averagedyn" + str(BITLENGTH) + str(N), averagearray)


def greedy(array, value):
    sum = 0
    elements = []
    array = sorted(array)
    for i in reversed(array):
        if sum + i <= value:
            sum = sum + i
            elements.append(i)
            # Remove the element that is added to the sum
            # del testarray[randomnum]
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
    write("AverageGreedy" + str(BITLENGTH) + str(N), averagearray)


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
        for i in range(1000):
            testset = randomSet(20)
            # N, set size = 20
            gotten, value = simulatedAnnealing(randomSet(20), random.randint(0, BITLENGTH), k)
            try:
                percent = gotten / float(value) * 100
            except:
                percent = 0
            arrayofpercent.append(percent)
        write2("simulatedAnnealing"+str(k), arrayofpercent, k)


exhaustive()
dynprog()
greedystart()
