# Generated by Django 4.2 on 2023-04-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0008_villa_photo4'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 3'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 4'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 5'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 3'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 4'),
        ),
    ]
