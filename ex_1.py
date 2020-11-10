import numpy as np
import scipy.io.wavfile
import sys
import copy
def main():
    sample,centroids=sys.argv[1],sys.argv[2]
    fs,y=scipy.io.wavfile.read(sample)
    x=np.array(y.copy())
    centroids=np.loadtxt(centroids)

    numberCentroids=centroids.shape #getting a tuple size of the centroids matrix (rows,columns). how many clusters=rows. 10,2
    pointsToTrain=x.shape #getting the number of points nedded to assign to a centroid (rows,columns). 32k,2
    distancePointCentroids=np.zeros((pointsToTrain[0],numberCentroids[0])) #matrix to store the distance of every point from the centroid. 32,10
    for i in range(distancePointCentroids[0]):
        for j in range(distancePointCentroids[1]):
            distancePointCentroids[i,j]=np.sqrt(()**2-()**2)






    oldCentroids=np.zeros(numberCentroids)
    nextCentroids=copy.deepcopy(centroids)

    isSameCentroids=False;
    Kclusters=np.zeros(pointsToTrain)

    print("hi")


    #scipy.io.wavfile.write("compressed.wav",fs,np.array(new_values,dtype=np.int16))


if __name__ == '__main__':
    main()
