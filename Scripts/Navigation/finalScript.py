import helpers
import time

cyclesInfo = [
    {
        "name": "cycle 0",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.60,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.3
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 0,
                "targetDistance": 0.93
            }
        ]
    },
    {
        "name": "cycle 1",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.60,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.30
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 0,
                "targetDistance": 0.93
            },
        ],
    },
    {
        "name": "cycle 2",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.6,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.3
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.89
            },
        ],
    },
    {
        "name": "cycle 3",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.6,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.8
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.89
            },
        ],
    },
    {
        "name": "cycle 4",
        "mainNavDirection": 270,
        "endOfCycleDistance": 0.6,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 270,
                "targetDistance": 0.30
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 180,
                "targetDistance": 0.30
            },
        ],
    },
    {
        "name": "cycle 5",
        "mainNavDirection": 90,
        "endOfCycleDistance": 0.6,
        "finalPoint": [
            {
                # horizontal navigation
                "name": "start point horizontal navigation",
                "lidarDirection": 90,
                "targetDistance": 0.3
            },
            {
                # vertical navigation
                "name": "start point vertical navigation",
                "lidarDirection": 0,
                "targetDistance": 0.3
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
