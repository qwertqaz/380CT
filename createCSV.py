def write(name, array):
    fo = open(name + ".csv", "wb")
    nloop = 1
    fo.write("n" + ',' + "Time in seconds" + ',' + '\n')
    for i in array:
        fo.write(str(nloop) + ',' + str(i) + ',' + '\n')
        nloop += 1
    fo.close()