from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from django.contrib import messages
from .models import Request
from datetime import datetime
from asgiref.sync import sync_to_async
from .utilities import *


async def calculator(request):
    if request.method == 'POST':
        total_distance = None
        time_elapsed = None

        start_timestamp = make_aware(datetime.now())

        points = get_input_points(request.POST)
        responses, error = await sync_to_async(request_distances)(points)

        end_timestamp = make_aware(datetime.now())
        time_elapsed = (end_timestamp-start_timestamp).total_seconds()
        total_distance = get_total_distance(responses)

        id = get_request_id(request.POST)
        request_record, _ = await sync_to_async(Request.objects.update_or_create)({'start_timestamp': start_timestamp, 'end_timestamp': end_timestamp}, request_id=id)

        print(request_record)
        print(f'DISTANCE CALCULATED: {total_distance}')

        if error:
            messages.error(request, 'An error occurred while calculating the distance. Please try again.')
            return redirect('calculator.html')

        context = {'total_distance': total_distance,
                'calculation_time': time_elapsed}

        return render(request, 'calculator.html', context)
    
    else:
        return render(request, 'calculator.html')
