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
    write("Averagedyn", averagearray)


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
    write("AverageGreedy", averagearray)

"""
def synapticAutism(array, value):
    for i in range(101):
        numberofsets = random.randint(0, len(array))
        total = 0
        oldtotal = 0
        print "v = ", value

        for k in range(numberofsets):
            total += array[k]

        print "t = ", total

        if total == value:
            return True

        if total > value:
            total = 0

        elif total < oldtotal:
            oldtotal = total

        else:
            print "nigga"
            continue
    return oldtotal
"""


def synapticAutism(array, value):
    sum = 0
    best = 0
    print array
    for t in range(101):
        testarray = array[:]
        for i in range(len(array)):
            randomnum = random.randint(0, len(testarray)-1)
            print testarray
            print sum
            if sum + testarray[randomnum] <= value:
                sum += testarray[randomnum]
                testarray.pop(randomnum)
            if sum == value:
                return "wow"
            if sum > best:
                best = sum
    return best, value, array

#print synapticAutism(randomSet(6), random.randint(0, BITLENGTH))
print synapticAutism([531, 553, 180, 520, 750, 666], 949)

