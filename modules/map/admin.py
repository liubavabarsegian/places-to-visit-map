from django.contrib import admin
from .models import Point

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time_create', 'fixed')
    list_filter = ('fixed', 'author')
    search_fields = ('title', 'short_description')
    actions = ['approve_points']

    def approve_points(self, request, queryset):
        queryset.update(fixed=True)
    approve_points.short_description = "Подтвердить выбранные точки"

# Register your models here.
