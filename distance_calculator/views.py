from django.shortcuts import render
from distance_calculator.forms import numberOfPointsForm


def calculatorInput(request):
    form = numberOfPointsForm()
    numberOfPointsValue = '2'

    if request.method == 'POST':
        form = numberOfPointsForm(request.POST)
        if form.is_valid():
            numberOfPointsValue = form.cleaned_data['numberOfPoints']

    context = {'numberOfPointsForm': form,
               'numberOfPoints': numberOfPointsValue}
    return render(request, 'calculator.html', context)
