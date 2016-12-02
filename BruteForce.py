from RandomSetGenerator import randomSet
import timeit

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


testset = randomSet(22)

start_time = timeit.default_timer()
print subsetsum(testset, 15)
elapsed = timeit.default_timer() - start_time

print elapsed