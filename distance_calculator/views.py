from django.shortcuts import render

def calculatorInput(request):
    return render(request, 'calculator.html')
