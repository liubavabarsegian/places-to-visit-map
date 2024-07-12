from django.shortcuts import render
from .models import Point
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def points_list(request):
    points = Point.objects.filter(fixed=True)
    points_json = serialize('json', points)
    return render(request, 'account/map.html', {'points_json': points_json})

@csrf_exempt
def add_point(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            short_description = request.POST.get('short_description')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            image = request.FILES.get('image')

            point = Point(
                title=title,
                short_description=short_description,
                latitude=latitude,
                longitude=longitude,
                images=image,
                author=request.user,
                fixed=False  # Устанавливаем fixed в False при создании
            )
            point.save()

            return JsonResponse({'success': True, 'message': 'Точка успешно добавлена и ожидает подтверждения.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# Create your views here.
