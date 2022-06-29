from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from distance_calculator.forms import numberOfPointsForm
from .models import Request
from datetime import datetime
import requests


def calculatorInput(request):
    NOPForm = numberOfPointsForm(request.POST or None)
    numberOfPoints = 2

    if request.method == 'POST':

        if 'setNumberOfPoints' in request.POST:
            NOPForm = numberOfPointsForm(request.POST)
            if NOPForm.is_valid():
                numberOfPoints = NOPForm.cleaned_data['numberOfPoints']

        if 'calculateDistance' in request.POST:
            inputRequestId = getRequestId(request.POST)
            inputPointsList = getCoordinates(request.POST)
            pointsString = serializePoints(inputPointsList)
            return redirect(processData, requestId=inputRequestId, pointsString=pointsString)

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPoints}

    return render(request, 'calculator.html', context)


def processData(request, requestId, pointsString):
    NOPForm = numberOfPointsForm(request.POST or None)
    numberOfPoints = 2
    distance = None
    timeElapsed = None

    if request.method == 'POST':

        if 'setNumberOfPoints' in request.POST:
            NOPForm = numberOfPointsForm(request.POST)
            if NOPForm.is_valid():
                numberOfPoints = NOPForm.cleaned_data['numberOfPoints']

        if 'calculateDistance' in request.POST:
            inputRequestId = getRequestId(request.POST)
            inputPointsList = getCoordinates(request.POST)
            pointsString = serializePoints(inputPointsList)
            return redirect(processData, requestId=inputRequestId, pointsString=pointsString)

    if request.method == 'GET':
        startTimestamp = make_aware(datetime.now())
        pointsList = deserializePoints(pointsString)
        distance = calculateDistance(pointsList)
        endTimestamp = make_aware(datetime.now())
        timeElapsed = (endTimestamp-startTimestamp).total_seconds()

        Request.objects.update_or_create(
            {'start_timestamp': startTimestamp, 'end_timestamp': endTimestamp}, request_id=requestId)

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPoints,
               'totalDistance': distance,
               'calculationTime': timeElapsed}

    return render(request, 'calculator.html', context)


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


def getDistanceBetweenPoints(originPoint, destinationPoint):
    requestString = f'http://146.59.46.40:60080/route?origin={originPoint[0]},{originPoint[1]}&destination={destinationPoint[0]},{destinationPoint[1]}'
    response = requests.get(requestString, auth=('Cristoforo', 'Colombo'))

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
