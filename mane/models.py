from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()

class Photo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Альбом')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    liked = models.IntegerField(default=0, verbose_name='Количество лайков')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'фотографию'
        verbose_name_plural = 'фотографии'

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()



