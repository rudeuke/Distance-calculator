from datetime import datetime
import asyncio
import aiohttp


def getRequestId(postRequest):
    requestId = postRequest.get('request_id')

    if requestId == '':
        timestamp = datetime.now()
        requestId = f'request {timestamp}'

    return requestId.replace(' ', '_')


def getCoordinates(postRequest):
    i = 1
    listOfPoints = []

    while True:
        latitude = postRequest.get(f'latitude{i}')
        longitude = postRequest.get(f'longitude{i}')
        i += 1

        if not latitude is None and not longitude is None:
            point = (latitude, longitude)
            listOfPoints.append(point)
        else:
            break

    return listOfPoints


def serializePoints(pointsList):
    pointsString = ''
    coordinatesList = []

    for point in pointsList:
        formattedPoint = ','.join(point)
        coordinatesList.append(formattedPoint)

    pointsString = '_'.join(coordinatesList)

    return pointsString


def deserializePoints(pointsString):
    listOfPoints = []
    for point in pointsString.split('_'):
        tempSet = (point.split(',')[0], point.split(',')[1])
        listOfPoints.append(tempSet)
    return listOfPoints


async def getDistanceBetweenPoints(session, originPoint, destinationPoint):
    requestString = f'http://146.59.46.40:60080/route?origin={originPoint[0]},{originPoint[1]}&destination={destinationPoint[0]},{destinationPoint[1]}'

    for _ in range(5):
        async with session.get(requestString) as response:
            try:
                jsonResponse = await response.json()

            except:
                continue

            else:
                try:
                    distanceCalculated = jsonResponse['distance']
                except:
                    error = jsonResponse['error']
                    print(f'response error: {error}')
                    return error
                else:
                    return distanceCalculated


async def calculateDistance(pointsList):
    actions = []

    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth('Cristoforo', 'Colombo')) as session:
        for i in range(1, len(pointsList)):
            actions.append(asyncio.ensure_future(
                getDistanceBetweenPoints(session, pointsList[i-1], pointsList[i])))

        responses = await asyncio.gather(*actions)

    try:
        totalDistance = sum(responses)
    except:
        return 'Error occured. Try again.', True
    else:
        return totalDistance, False
