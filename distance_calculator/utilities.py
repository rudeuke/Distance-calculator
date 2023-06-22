from datetime import datetime
import json
import time
from django.urls import reverse
import requests
import concurrent.futures


def get_request_id(post_request):
    request_id = post_request.get('request_id')

    if request_id == '':
        timestamp = datetime.now()
        request_id = f'request {timestamp}'

    return request_id.replace(' ', '_')


def get_input_points(post_request):
    try:
        points_count = sum(key.startswith('latitude-') for key in post_request)
    except:
        return None
    
    points = []
    for i in range(1, points_count+1):
        point = {
            'latitude': post_request.get(f'latitude-{i}'),
            'longitude': post_request.get(f'longitude-{i}'),
        }
        points.append(point)

    return points


def get_segments_from_points(points):
    points_count = len(points)
    segments = []

    for i in range(points_count-1):
        segment = {
            'lat1': points[i]['latitude'],
            'lon1': points[i]['longitude'],
            'lat2': points[i+1]['latitude'],
            'lon2': points[i+1]['longitude'],
        }
        segments.append(segment)
        
    return segments


def try_fetch_data(url, params):
    max_retries = 3
    retry_delay = 0.5

    for retry in range(max_retries):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f'Error: {e}')
            print(f'Retrying request for URL: {url} (retry {retry+1}/{max_retries})')
            time.sleep(retry_delay)

    return None


def request_distances(points):
    segments = get_segments_from_points(points)
    api_url = reverse('distance-api:calculate-distance')
    full_url = 'http://127.0.0.1:8000' + api_url
    results = []
    error = False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(try_fetch_data, full_url, params=params) for params in segments]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(json.loads(result))
            except Exception as e:
                print(f'Error: {e}')
                error = True
                return None, error

    return results, error


def get_total_distance(responses):
    total_distance = 0
    for response in responses:
        try:
            distance = float(response["distance"])
        except:
            print(f'Error parsing response: {response}')
            return None
        
        total_distance += distance

    return total_distance