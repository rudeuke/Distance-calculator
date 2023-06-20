from rest_framework.decorators import api_view
from django.http import JsonResponse
from geopy.distance import geodesic

@api_view(['GET'])
def calculate_distance(request):
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