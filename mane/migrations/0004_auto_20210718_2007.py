# Generated by Django 3.2.4 on 2021-07-18 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mane', '0003_auto_20210718_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mane.album', verbose_name='Альбом'),
        ),
    ]
