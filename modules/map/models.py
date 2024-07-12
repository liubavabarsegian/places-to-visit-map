from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Point(models.Model):
    """
    Модель точек для сайта
    """    

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    latitude = models.FloatField(verbose_name='Широта', default=0)
    longitude = models.FloatField(verbose_name='Долгота', default=0)
    short_description = models.TextField(verbose_name='Краткое описание', max_length=500)
    full_description = models.TextField(verbose_name='Полное описание')
    images = models.ImageField(
        verbose_name='Превью точки', 
        blank=True, 
        upload_to='images/', 
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    fixed = models.BooleanField(verbose_name='Зафиксировано', default=False)

    class Meta:
        db_table = 'app_points'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create'])]
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.title

# Create your models here.
