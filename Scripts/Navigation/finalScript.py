import helpers
import time

cyclesInfo = [
    {
        "name": "cycle 0",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.40
            }
        ]
    },
    {
        "name": "cycle 1",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 0,
                "targetDistance": 0.40
            },
        ],
    },
    {
        "name": "cycle 2",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.40
            },
        ],
    },
    {
        "name": "cycle 3",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.40
            },
        ],
    },
    {
        "name": "cycle 4",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.15
            },
        ],
    },
    {
        "name": "cycle 5",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.20,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.15
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.15
            },
        ],
    },  
]

allCyclesFinished = False

while True:
    
    if not allCyclesFinished:
        helpers.start(cyclesInfo)
        
    print('navigation ended')
    time.sleep(10)
