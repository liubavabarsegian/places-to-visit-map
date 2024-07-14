from django.shortcuts import render, redirect
from .models import Point
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from django.views.generic import ListView
from .models import Point


class PointsListView(ListView):
    model = Point
    template_name = 'account/map.html'
    context_object_name = 'points'

    def get_queryset(self):
        return Point.objects.filter(fixed=True)

    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)
        points = self.get_queryset()
        points_json = serialize('json', points)
        context['points_json'] = points_json
        context['form'] = CommentCreateForm()
        return context


@csrf_exempt
def add_point(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            short_description = request.POST.get('short_description')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            image = request.FILES.get('image')

            if not latitude or not longitude:
                return JsonResponse({'success': False, 'error': 'Пожалуйста, выберите точку на карте.'})

            point = Point(
                title=title,
                short_description=short_description,
                latitude=latitude,
                longitude=longitude,
                images=image,
                author=request.user,
                fixed=False
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

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentCreateForm
from .models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm

    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def form_invalid(self, form):
        if self.is_ajax():
            return JsonResponse({'error': form.errors}, status=400)
        return super().form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.point_id = self.kwargs.get('pk')
        comment.author = self.request.user
        comment.parent_id = form.cleaned_data.get('parent')
        comment.save()

        if self.is_ajax():
            return JsonResponse({
                'is_child': comment.is_child_node(),
                'id': comment.id,
                'author': comment.author.username,
                'parent_id': comment.parent_id,
                'time_create': comment.time_create.strftime('%Y-%b-%d %H:%M:%S'),
                'content': comment.content,
                'get_absolute_url': comment.author.profile.get_absolute_url()
            }, status=200)

        return redirect(comment.point.get_absolute_url())

    def handle_no_permission(self):
        return JsonResponse({'error': 'Необходимо авторизоваться для добавления комментариев'}, status=400)

# Create your views here.