import numpy as np
import scipy.io.wavfile
import sys
import copy


def main():
    #opening file output.txt to write
    outputFile = open(f"output.txt", "w")
    sample, centroids = sys.argv[1], sys.argv[2]
    fs, y = scipy.io.wavfile.read(sample)
    x = np.array(y.copy())
    centroids = np.loadtxt(centroids)
    iter = 0;
    numberCentroids = centroids.shape  # getting a tuple size of the centroids matrix (rows,columns). how many clusters=rows. 10,2
    pointsToTrain = x.shape  # getting the number of points nedded to assign to a centroid (rows,columns). 32k,2
    distancePointCentroids = np.zeros(
        (pointsToTrain[0], numberCentroids[0]))  # matrix to store the distance of every point from the centroid. 32K,10

    Kclusters = np.zeros(pointsToTrain[0])  # the array that contains  32k,2-zero array
    pervList = np.copy(centroids)
    list = np.copy(centroids)
    #if falg would be numberCentroids then we have the same iter twice results
    flag = 1
    while iter < 30 and flag < numberCentroids[0]:
        flag = 0
        iter += 1
        # calculating the distance
        for i in range(pointsToTrain[0]):
            for j in range(numberCentroids[0]):
                distancePointCentroids[i, j] = np.sqrt(((x[i][0] - list[j][0]) ** 2) + ((x[i][1] - list[j][1])) ** 2)
        # taking the min distance out of the 10 colums
        Kclusters = np.argmin(distancePointCentroids, axis=1)
        pervList = np.copy(list)
        # calculating mean of the clusters
        for i in range(numberCentroids[0]):
            check = False
            sumX = 0
            sumY = 0
            cntr = 0
            for j in range(pointsToTrain[0]):
                if Kclusters[j] == i:
                    check = True
                    sumX += x[j][0]
                    sumY += x[j][1]
                    cntr += 1
            temp1 = sumX / cntr
            temp2 = sumY / cntr
            roundTemp1 = np.round(temp1)
            roundTemp2 = np.round(temp2)
            if check:
                list[i] = [roundTemp1, roundTemp2]
        print(f"[iter {iter - 1}]:{','.join([str(i) for i in list])}\n")
        outputFile.write(f"[iter {iter - 1}]:{','.join([str(i) for i in list])}\n")

        # compare to pervlist and list ,if its the same stop the while
        for i in range(numberCentroids[0]):
            if list[i][0] == pervList[i][0]:
                if list[i][1] == pervList[i][1]:
                    #summing the numer of points that is the same from the prev iter
                    flag += 1
    outputFile.close()

if __name__ == '__main__':
    main()
