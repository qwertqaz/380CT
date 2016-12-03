def write(name, array):
    fo = open(name + ".csv", "wb")
    nloop = 1
    fo.write("n" + ',' + "Time in seconds" + ',' + '\n')
    for i in array:
        fo.write(str(nloop) + ',' + str(i) + ',' + '\n')
        nloop += 1
    fo.close()


def write2(name, array, length):
    fo = open(name + ".csv", "wb")
    fo.write("Loops" + ',' + "Percent of total" + ',' + '\n')
    for i in array:
        fo.write(str(length) + ',' + str(i) + ',' + '\n')
    fo.close()