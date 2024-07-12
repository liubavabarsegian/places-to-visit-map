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


from django.contrib.auth.decorators import login_required

@login_required
def toggle_favorite(request, point_id):
    point = Point.objects.get(id=point_id)
    user = request.user
    if point in user.favorite_points.all():
        user.favorite_points.remove(point)
        return JsonResponse({'status': 'removed'})
    else:
        user.favorite_points.add(point)
        return JsonResponse({'status': 'added'})
    

@login_required
def favorite_points(request):
    points = request.user.favorite_points.all()
    return render(request, 'account/favorite_points.html', {'points': points})

# Create your views here.
