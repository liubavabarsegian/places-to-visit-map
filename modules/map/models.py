from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


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
    fixed = models.BooleanField(verbose_name='Подтверждено', default=False)
    favorited_by = models.ManyToManyField(User, related_name='favorite_points', blank=True)

    def get_absolute_url(self):
        return reverse('points_list') + f'#point-{self.pk}'

    class Meta:
        db_table = 'app_points'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create'])]
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.title
    
from django.db import models
from django.contrib.auth import get_user_model

from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Comment(MPTTModel):
    """
    Модель древовидных комментариев
    """

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    point = models.ForeignKey(Point, on_delete=models.CASCADE, verbose_name='Точка', related_name='comments')
    author = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE, related_name='comments_author')
    content = models.TextField(verbose_name='Текст комментария', max_length=3000)
    time_create = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
    parent = TreeForeignKey('self', verbose_name='Родительский комментарий', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MTTMeta:
        order_insertion_by = ('-time_create',)

    class Meta:
        db_table = 'app_comments'
        indexes = [models.Index(fields=['-time_create', 'time_update', 'status', 'parent'])]
        ordering = ['-time_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}:{self.content}'

# Create your models here.
