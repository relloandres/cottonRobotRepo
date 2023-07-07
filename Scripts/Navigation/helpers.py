import numpy as np
from adafruit_rplidar import RPLidar
import math
import time
import csv
import json

def getLidarData(maxScans):
    # Setup the RPLidar
    PORT_NAME = '/dev/ttyUSB0'
    lidar = RPLidar(None, PORT_NAME, timeout=3)

    data = []
    scansIter = 0
    
    # Read data
    for scan in lidar.iter_scans():
        scansIter = scansIter+1
        for (_, angle, distance) in scan:
            data.append([distance/1000, angle])
        if (scansIter == maxScans):
            break

    # Turn off lidar
    lidar.stop()
    lidar.disconnect()
    
    return np.array(data)

def getPolarProjection(a, b):
    #Get projection of a onto b
    r1, theta1 = a
    r2, theta2 = b

    # Calculate the dot product
    dotProduct = r1 * r2 * math.cos((theta1 - theta2)*math.pi/180)

    return abs(dotProduct/r2)

def findWallPoints(direction, thetaRange, polarData, sigmas = 2):
    #direction common values
    #0   (sud)
    #90  (east)
    #180 (nord)
    #270 (west)
    
    theta1 = direction - thetaRange
    theta2 = direction + thetaRange
    
    #Select all points in the specified direction
    if theta1 < 0:
        theta1 = theta1 % 360
        wallPoints = polarData[(polarData[:, 1] >= theta1) | (polarData[:, 1] <= theta2)]
    else:
        wallPoints = polarData[(polarData[:, 1] >= theta1) & (polarData[:, 1] <= theta2)]
        
    #Filter noise based on distance in specified direction
    d = np.zeros(wallPoints.shape[0])
    for i,point in enumerate(wallPoints):
        d[i] = getPolarProjection(point, [1,direction])

    # Calculate the mean and standard deviation of projections
    mean = np.mean(d)
    std = np.std(d)

    # Create a boolean mask for elements within the specified range
    mask = np.abs(d - mean) <= sigmas * std

    # Get the indices of the elements that satisfy the mask
    indices = np.where(mask)[0]

    return wallPoints[indices]

def getDistanceFromWall(direction, thetaRange, polarData, sigmas = 2):
    #direction common values
    #0   (sud)
    #90  (east)
    #180 (nord)
    #270 (west)
    
    wallPoints = findWallPoints(direction, thetaRange, polarData, sigmas)
    return findWallPoints(direction, thetaRange, polarData, sigmas)[np.argmin(np.abs(wallPoints[:,1] - direction))][0]
    
def sudoPublishLidarData(lidarData):
    # json.dumps(a.tolist())
    return

def sudoPublishNavigationCommand(command):
    print(f"[sudoPublishNavigationCommand] command: {command}")
    return

def setOrientationUsingWall(direction):
    print(f"Setting orientation using {direction} direction")
    return

def navigationCommand(command, magnitude, timeOut=-1):
    sudoCommand = f"{command};{magnitude}"
    if timeOut>0:
        sudoPublishNavigationCommand(sudoCommand)
        print(f"[navigationCommand] command: ({sudoCommand}, {timeOut})")
        time.sleep(timeOut)
        sudoPublishNavigationCommand('stop;0')
    else:
        print(f"[navigationCommand] command: {sudoCommand}")
        sudoPublishNavigationCommand(sudoCommand)
    return

def navigateUsingWall(wallDirection, targetDistance):
    print(f"[navigateUsingWall] ({wallDirection},{targetDistance})")
    
    lidarData = getLidarData(5)
    currentDistance = getDistanceFromWall(wallDirection, 2, lidarData)
    
    # 1 implies move closer to wall, -1 implies move away from the wall
    navDirection = int(math.copysign(1,currentDistance - targetDistance))
    
    if wallDirection==0:
        if navDirection>0:
            navigationCommand('backward', 0.1)
        else:
            navigationCommand('forward', 0.1)
    elif wallDirection==180:
        if navDirection>0:
            navigationCommand('forward', 0.1)
        else:
            navigationCommand('backward', 0.1)
    elif wallDirection==90:
        if navDirection>0:
            navigationCommand('right', 0.1)
        else:
            navigationCommand('left', 0.1)
    elif wallDirection==270:
        if navDirection>0:
            navigationCommand('left', 0.1)
        else:
            navigationCommand('right', 0.1)
        
    while navDirection*(currentDistance - targetDistance) > 0.02:
        print(f"[navigateUsingWall] currentDistance: {currentDistance}")
        lidarData = getLidarData(5)
        currentDistance = getDistanceFromWall(wallDirection, 2, lidarData)
        print(f"[navigateUsingWall] currentDistance: {currentDistance}")
    
    navigationCommand('stop', 0)
    print("[navigateUsingWall] navigation ended")

def isEndOfCycle(lidarData, wallDirection, threshold):
    '''
    This method process lidar data and returns True when the distance of the lidar and the wall (in the specified direction)
    is smaller than the specified threshold
    '''
    distanceFromWall = getDistanceFromWall(wallDirection, 2, lidarData)
    print(f"[isEndOfCycle] distanceFromWall: {distanceFromWall}")
    if distanceFromWall<=threshold:
        return True
    return False
    
def start(cyclesInfo):
    
    for cycleInfo in cyclesInfo:
        print(f"------- Starting {cycleInfo['name']} -------")
        
        # set variables used during the cycle
        endOfCycle = False
        
        if cycleInfo['mainNavDirection'] == 90:
            mainNavCommand = 'right'
        else:
            mainNavCommand = 'left'

        #Start navigation
        navigationCommand(mainNavCommand, 0.1)
        
        while (not endOfCycle):                
            # Check end of cycle
            lidarData = getLidarData(5)
            endOfCycle = isEndOfCycle(lidarData, cycleInfo['mainNavDirection'], cycleInfo['endOfCycleDistance'])
            
        navigationCommand("stop", 0)
        
        time.sleep(1)
        
        # Horizontal Navigation
        navigateUsingWall(cycleInfo['finalPoint'][0]['lidarDirection'], cycleInfo['finalPoint'][0]['targetDistance'])
        
        time.sleep(1)
        
        # Vertical Navigation
        navigateUsingWall(cycleInfo['finalPoint'][1]['lidarDirection'], cycleInfo['finalPoint'][1]['targetDistance'])
