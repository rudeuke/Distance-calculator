from django.shortcuts import render
from distance_calculator.forms import numberOfPointsForm, pointForm
import requests


def calculatorInput(request):
    NOPForm = numberOfPointsForm()
    ptForm = pointForm()
    numberOfPointsValue = '2'

    if request.method == 'POST':
        NOPForm = numberOfPointsForm(request.POST)
        if NOPForm.is_valid():
            numberOfPointsValue = NOPForm.cleaned_data['numberOfPoints']

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPointsValue,
               'pointForm': ptForm}

    return render(request, 'calculator.html', context)


def processData(request, temp1, pointsString):
    NOPForm = numberOfPointsForm()
    PForm = pointForm()
    numberOfPointsValue = '2'

    if request.method == 'POST':
        NOPForm = numberOfPointsForm(request.POST)
        if NOPForm.is_valid():
            numberOfPointsValue = NOPForm.cleaned_data['numberOfPoints']

    if request.method == 'GET':
        pointsList = serializePoints(pointsString)
        distance = calculateDistance(pointsList)
        print(distance)

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPointsValue,
               'pointForm': PForm,
               'totalDistance': distance}

    return render(request, 'calculator.html', context)


def serializePoints(pointsString):
    listOfPoints = []
    for point in pointsString.split('_'):
        tempSet = (point.split(',')[0], point.split(',')[1])
        listOfPoints.append(tempSet)
    return listOfPoints


def getDistanceBetweenPoints(originPoint, destinationPoint):
    requestString = f'http://146.59.46.40:60080/route?origin={originPoint[0]},{originPoint[1]}&destination={destinationPoint[0]},{destinationPoint[1]}'
    response = requests.get(requestString, auth=('Cristoforo', 'Colombo'))
    return response.json()['distance']


def calculateDistance(pointsList):
    totalDistance = 0
    for i in range(1, len(pointsList)):
        partialDistance = getDistanceBetweenPoints(
            pointsList[i-1], pointsList[i])
        totalDistance += partialDistance
    return totalDistance
