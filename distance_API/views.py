from rest_framework.decorators import api_view
from django.http import JsonResponse
from geopy.distance import geodesic
from time import sleep
from random import randint


@api_view(['GET'])
def calculate_distance(request):
    simulate_request_delay()

    try:
        lat1 = float(request.GET.get('lat1'))
        lon1 = float(request.GET.get('lon1'))
        lat2 = float(request.GET.get('lat2'))
        lon2 = float(request.GET.get('lon2'))
        decimal_places = int(request.GET.get('dec', 3))

        point1 = (lat1, lon1)
        point2 = (lat2, lon2)

        distance = round(geodesic(point1, point2).kilometers, decimal_places)
        return JsonResponse({'distance': distance})
    
    except (TypeError, ValueError) as e:
        return JsonResponse({'error': f'Invalid coordinates provided. {e}'}, status=400)
    

def simulate_request_delay():
    r = randint(50, 170)
    simulated_delay_time = float(r / 100)
    sleep(simulated_delay_time)