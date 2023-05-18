# Generated by Django 4.2 on 2023-05-08 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0011_villaphotos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_photos',
        ),
        migrations.RemoveField(
            model_name='yacht',
            name='yacht_photos',
        ),
        migrations.AddField(
            model_name='vehiclephotos',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacation.vehicle', verbose_name='Автомобиль'),
        ),
        migrations.AddField(
            model_name='yachtphotos',
            name='yacht',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacation.yacht', verbose_name='Яхта'),
        ),
    ]