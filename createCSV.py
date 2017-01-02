def write(name, array):
    fo = open(name + ".csv", "wb")
    nloop = 1
    fo.write("n" + ',' + "Time in seconds" + ',' + '\n')
    for i in array:
        fo.write(str(nloop) + ',' + str(i) + ',' + '\n')
        nloop += 1
    fo.close()


def write2(name, array, array2, length):
    fo = open("simulated.csv", "a")
    avg = sum(array) / float(len(array))
    avg2 = sum(array2) / float(len(array2))
    fo.write(str(length) + ',' + str(avg) + ',' + str(avg2) + ',' + '\n')
    fo.close()


def write3(name, array, length):
    fo = open(name + ".csv", "a")
    avg = sum(array) / float(len(array))
    fo.write(str(length) + ',' + str(avg) + ',' + '\n')
    fo.close()


def write4(name, array, array2, length):
    fo = open(name + ".csv", "a")
    avg = sum(array) / float(len(array))
    avg2 = sum(array2) / float(len(array2))
    fo.write(str(length) + ',' + str(avg) + ',' + str(avg2) + ',' + '\n')
    fo.close()