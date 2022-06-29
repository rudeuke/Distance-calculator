from django.shortcuts import redirect, render
from distance_calculator.forms import numberOfPointsForm, pointForm
from datetime import datetime
import requests


def calculatorInput(request):
    NOPForm = numberOfPointsForm(request.POST or None)
    PForm = pointForm()
    numberOfPoints = 2

    if request.method == 'POST':

        if 'setNumberOfPoints' in request.POST:
            NOPForm = numberOfPointsForm(request.POST)
            if NOPForm.is_valid():
                numberOfPoints = NOPForm.cleaned_data['numberOfPoints']

        if 'calculateDistance' in request.POST:
            inputPointsList = getCoordinates(request.POST)
            pointsString = serializePoints(inputPointsList)
            return redirect(processData, temp1='tempValue', pointsString=pointsString)

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPoints,
               'pointForm': PForm}

    return render(request, 'calculator.html', context)


def processData(request, temp1, pointsString):
    NOPForm = numberOfPointsForm(request.POST or None)
    PForm = pointForm()
    numberOfPoints = 2
    distance = None
    timeElapsed = None

    if request.method == 'POST':

        if 'setNumberOfPoints' in request.POST:
            NOPForm = numberOfPointsForm(request.POST)
            if NOPForm.is_valid():
                numberOfPoints = NOPForm.cleaned_data['numberOfPoints']

        if 'calculateDistance' in request.POST:
            inputPointsList = getCoordinates(request.POST)
            pointsString = serializePoints(inputPointsList)
            return redirect(processData, temp1='tempValue', pointsString=pointsString)

    if request.method == 'GET':
        start_timestamp = datetime.now()
        print(f'start_timestamp: {start_timestamp}')

        pointsList = deserializePoints(pointsString)
        distance = calculateDistance(pointsList)
        print(distance)

        end_timestamp = datetime.now()
        print(f'end_timestamp: {end_timestamp}')

        timeElapsed = (end_timestamp-start_timestamp).total_seconds()

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPoints,
               'pointForm': PForm,
               'totalDistance': distance,
               'calculationTime': timeElapsed}

    return render(request, 'calculator.html', context)


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


def getDistanceBetweenPoints(originPoint, destinationPoint):
    requestString = f'http://146.59.46.40:60080/route?origin={originPoint[0]},{originPoint[1]}&destination={destinationPoint[0]},{destinationPoint[1]}'
    print(f'request string: {requestString}')
    response = requests.get(requestString, auth=('Cristoforo', 'Colombo'))
    print(f'response: {str(response.json())}')

    try:
       distanceCalculated = response.json()['distance']
    except:
        error = response.json()['error']
        print(f'response error: {error}')
        return error
    else:
        return distanceCalculated


def calculateDistance(pointsList):
    totalDistance = 0
    for i in range(1, len(pointsList)):
        partialDistance = getDistanceBetweenPoints(
            pointsList[i-1], pointsList[i])

        try:
            totalDistance += partialDistance
        except:
            return f'Error occured: {partialDistance}'

    return totalDistance
