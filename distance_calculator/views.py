from django.shortcuts import render
from django.utils.timezone import make_aware
from django.contrib import messages
from .models import Request
from datetime import datetime
from asgiref.sync import sync_to_async
from .utilities import *
from django.http import JsonResponse


async def calculator(request):
    if request.method == 'POST':
        points = get_input_points(request.POST)

        start_timestamp = make_aware(datetime.now())
        responses, error = await sync_to_async(request_distances)(points)
        end_timestamp = make_aware(datetime.now())

        time_elapsed = (end_timestamp-start_timestamp).total_seconds()
        total_distance = get_total_distance(responses)

        id = get_request_id(request.POST)
        request_record, _ = await sync_to_async(Request.objects.update_or_create)({'start_timestamp': start_timestamp, 'end_timestamp': end_timestamp}, request_id=id)

        if error:
            messages.error(request, 'An error occurred while calculating the distance. Please try again.')
            return JsonResponse({'success': False})
        
        print(request_record)
        print(f'DISTANCE CALCULATED: {total_distance}')

        response_data = {
            'total_distance': total_distance,
            'calculation_time': time_elapsed,
        }
        return JsonResponse(response_data)
    
    else:
        return render(request, 'calculator.html')