import numpy as np
import scipy.io.wavfile
import sys
import copy
def main():
    sample,centroids=sys.argv[1],sys.argv[2]
    fs,y=scipy.io.wavfile.read(sample)
    x=np.array(y.copy())
    centroids=np.loadtxt(centroids)
    iter=0;
    numberCentroids=centroids.shape #getting a tuple size of the centroids matrix (rows,columns). how many clusters=rows. 10,2
    pointsToTrain=x.shape #getting the number of points nedded to assign to a centroid (rows,columns). 32k,2
    distancePointCentroids=np.zeros((pointsToTrain[0],numberCentroids[0])) #matrix to store the distance of every point from the centroid. 32K,10

    Kclusters = np.zeros(pointsToTrain[0]) #the array that contains  32k,2-zero array

    #calcluting the distance
    for i in range(pointsToTrain[0]):
        for j in range(numberCentroids[1]):
            distancePointCentroids[i,j]=np.sqrt(((x[i][0]-centroids[j][0])**2)+((x[i][1]-centroids[j][1]))**2)

    #taking the min distance out of the 10 colums
    for i in range(pointsToTrain[0]):
        minDist = distancePointCentroids[i, 0];
        minCluster = 0;
        for j in range(numberCentroids[0]):
            if minDist>distancePointCentroids[i,j]:
                minDist = distancePointCentroids[i, j];
                minCluster=j;
                Kclusters[i]=j;

    outputFile=open("output.txt","w")
    outputFile.write(f"[iter {iter}]:{','.join([str(i) for i in centroids])}")
    outputFile.close()


    # oldCentroids=np.zeros(numberCentroids)
    # nextCentroids=copy.deepcopy(centroids)
    #
    # isSameCentroids=False;


    #scipy.io.wavfile.write("compressed.wav",fs,np.array(new_values,dtype=np.int16))


if __name__ == '__main__':
    main()
