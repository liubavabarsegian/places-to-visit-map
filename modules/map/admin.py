from django.contrib import admin
from .models import Point

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time_create', 'fixed')
    list_filter = ('fixed', 'author')
    search_fields = ('title', 'short_description')
    actions = ['approve_points']
    filter_horizontal = ('favorited_by',)  # Это позволит выбирать пользователей вручную

    def approve_points(self, request, queryset):
        queryset.update(fixed=True)
    approve_points.short_description = "Подтвердить выбранные точки"

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # Если это новый объект
            fields = [f for f in fields if f != 'favorited_by']
        return fields

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Если это новый объект
            obj.favorited_by.clear()  # Очищаем поле favorited_by после сохранения


from mptt.admin import DraggableMPTTAdmin
from .models import Comment

@admin.register(Comment)
class CommentAdminPage(DraggableMPTTAdmin):
    """
    Админ-панель модели комментариев
    """
    list_display = ('tree_actions', 'indented_title', 'point', 'author', 'time_create', 'status')
    mptt_level_indent = 2
    list_display_links = ('point',)
    list_filter = ('time_create', 'time_update', 'author')
    list_editable = ('status',)
# Register your models here.
