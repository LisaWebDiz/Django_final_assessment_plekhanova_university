# Generated by Django 4.2 on 2023-04-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0006_alter_vehicle_vehicle_photos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='villa',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='villa',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='villa',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]