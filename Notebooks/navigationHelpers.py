import csv
import numpy as np

# General functions

def getLidarData(filePath, maxDistance=1.5, minDistance=0.15, maxTheta=360, minTheta=0):
    '''
    This method gets lidar and optionally performs tow types of filters based on distance and direction using polar coordinates. 
    To filter by distance the params maxDistance and minDistance are used. To filter by direction the params maxTheta and minTheta
    are used. When filtering by direction contains points around 0 then minTheta>maxTheta. For example if we want points between 
    350 and 10, maxTheta=10 and minTheta=350. Otehrwise  minTheta<maxTheta.
    '''
    angularFilteringType = 0 if minTheta-maxTheta<0 else 1
    print(angularFilteringType)
    polarLidarData = []
    with open(filePath, 'r') as file: 
        csvReader = csv.reader(file)

        for row in csvReader:
            r = float(row[1])/1000
            theta = float(row[0])
            if (minDistance < r < maxDistance):
                if (angularFilteringType==1):
                    if (theta>=minTheta or theta<=maxTheta):
                        polarLidarData.append([r,theta])
                else:
                    if (minTheta<=theta<=maxTheta):
                        polarLidarData.append([r,theta])

    return np.array(polarLidarData)

def getLidarData2(filePath, maxDistance=1.5, minDistance=0.15, maxTheta=[360], minTheta=[0]):
    '''
    This method works similar to getLidarData, but differs in the following:
    1) directional filtering can be done for more than one interval. maxTheta and minTheta are arrays with the same number of 
    elements.The nth element of each array will define the nth valid interval.
    2) the method returns an array with the same number of elements as intervals defined, each element contains the points of the
    corresponding interval. 
    '''

    polarLidarData = []
    for i in range(len(maxTheta)):
        polarLidarData.append([])
        
    with open(filePath, 'r') as file: 
        csvReader = csv.reader(file)

        for row in csvReader:
            r = float(row[1])/1000
            theta = float(row[0])
            
            # filter by distance
            if (minDistance < r < maxDistance):
                
                # filter by direction
                for i,(Mt, mt) in enumerate(zip(maxTheta, minTheta)):
                    angularFilteringType = 0 if mt-Mt<0 else 1
                    
                    if (angularFilteringType==1):
                        if (theta>=mt or theta<=Mt):
                            polarLidarData[i].append([r,theta])
                    else:
                        if (mt<=theta<=Mt):
                            polarLidarData[i].append([r,theta])

    return polarLidarData

# Rotation 

def getRotationAngle(lidarData, mainDirection):
    '''This function returns the difference in degrees between two angles. The first angle is defined using mainDirection. The 
    second angle corresponds to that of the point that is closer to the robot.'''
    
    mainDirectionPointIdx = np.abs(lidarData[:,1]-mainDirection).argmin()
    closestPointDirectionIdx = lidarData[:,0].argmin()
    
    boundaryFound = True if np.abs(lidarData[mainDirectionPointIdx,1] - lidarData[closestPointDirectionIdx,1])>180 else False
    
    if boundaryFound:
        return lidarData[mainDirectionPointIdx,1] - (lidarData[closestPointDirectionIdx,1]-360)
    else:
        return lidarData[mainDirectionPointIdx,1] - lidarData[closestPointDirectionIdx,1]
    
def getRotationAnglePts(lidarData, mainDirection):
    '''
    This method returns an array with two elements. This elements corresponds to the indexes of lidarData for (1) the point
    in mainDirection and (2) the closest point to the robot'''
    
    mainDirectionPointIdx = np.abs(lidarData[:,1]-mainDirection).argmin()
    closestPointDirectionIdx = lidarData[:,0].argmin()
        
    return [mainDirectionPointIdx,closestPointDirectionIdx]