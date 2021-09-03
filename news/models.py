from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории новостей')
    is_active =  models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()

class News (models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория новости')
    intro = models.TextField(verbose_name='Введение')
    body = models.TextField(verbose_name='Новость')
    image = models.ImageField(upload_to='news/', verbose_name='Картинка')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name='Дата публикации')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()