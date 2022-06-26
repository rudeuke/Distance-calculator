from django.shortcuts import render
from distance_calculator.forms import numberOfPointsForm, pointForm


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
