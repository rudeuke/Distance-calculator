from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from django.contrib import messages
from distance_calculator.forms import numberOfPointsForm
from .models import Request
from datetime import datetime
from asgiref.sync import sync_to_async
from .utilities import *


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


async def processData(request, requestId, pointsString):
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
        pointsList = deserializePoints(pointsString)
        startTimestamp = make_aware(datetime.now())

        distance, calculationError = await calculateDistance(pointsList)
        if calculationError:
            messages.error(request, distance)
            return redirect(calculatorInput)

        endTimestamp = make_aware(datetime.now())
        timeElapsed = (endTimestamp-startTimestamp).total_seconds()

        requestRecord, _ = await sync_to_async(Request.objects.update_or_create)({'start_timestamp': startTimestamp, 'end_timestamp': endTimestamp}, request_id=requestId)
        print(requestRecord)
        print(f'DISTANCE CALCULATED: {distance}')

    context = {'numberOfPointsForm': NOPForm,
               'numberOfPoints': numberOfPoints,
               'totalDistance': distance,
               'calculationTime': timeElapsed}

    return render(request, 'calculator.html', context)
