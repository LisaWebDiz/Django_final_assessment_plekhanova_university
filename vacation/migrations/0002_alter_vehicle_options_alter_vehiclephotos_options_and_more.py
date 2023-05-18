# Generated by Django 4.2 on 2023-04-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['-price_per_day'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='vehiclephotos',
            options={'verbose_name': 'Фотография автомобиля', 'verbose_name_plural': 'Фотографии автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='villa',
            options={'ordering': ['-price_per_day'], 'verbose_name': 'Вилла', 'verbose_name_plural': 'Виллы'},
        ),
        migrations.AlterModelOptions(
            name='yacht',
            options={'ordering': ['-price_per_day'], 'verbose_name': 'Яхта', 'verbose_name_plural': 'Яхты'},
        ),
    ]