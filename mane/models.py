from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

class Photo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Альбом')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    liked = models.IntegerField(default=0, verbose_name='Количество лайков')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'фотографию'
        verbose_name_plural = 'фотографии'


class News_Bloc(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Введение')

class News(models.Model):
    news_type = models.CharField(max_length=150, verbose_name='Тип новости')
    title = models.CharField(max_length=150, verbose_name='Заголовок новости')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    news = models.TextField(blank=True, null=True, verbose_name='Описание новости')
    date_creat = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',blank=True, null=True)
    date_public = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации',blank=True, null=True)


