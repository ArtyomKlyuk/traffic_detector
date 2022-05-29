# Generated by Django 4.0.4 on 2022-05-29 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConformityCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Номер свидетельства')),
                ('expirationDate',
                 models.DateField(max_length=50, verbose_name='Срок действия свидетельства в формате ISO8601')),
            ],
        ),
        migrations.CreateModel(
            name='GpsCoord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Шиирота. В градусах.')),
                ('longitude', models.FloatField(verbose_name='Долгота. В градусах.')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(verbose_name='x координата')),
                ('y', models.IntegerField(verbose_name='y координата')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=512, verbose_name='Адрес зоны обзора')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detector.gpscoord')),
                ('vrpDetectionArea',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detector.point')),
            ],
        ),
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=50, verbose_name='Серийный номер')),
                ('model', models.CharField(max_length=50, verbose_name='Производитель')),
                ('address', models.CharField(max_length=512, verbose_name='Адрес установки')),
                ('state', models.CharField(choices=[('NEW', 'Новый'), ('SETUP', 'Настройка'), ('ACTIVE', 'Активный')],
                                           max_length=20, verbose_name='Режим работы детектора')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detector.zone')),
            ],
        ),
    ]