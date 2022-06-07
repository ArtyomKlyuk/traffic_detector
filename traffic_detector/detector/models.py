from django.db import models



class ConformityCertificate(models.Model):
    """Свидетельство средства измерения"""
    number = models.CharField(verbose_name='Номер свидетельства', max_length=50)
    expirationDate = models.DateField(verbose_name='Срок действия свидетельства в формате ISO8601', max_length=50)


class Point(models.Model):
    x = models.IntegerField(verbose_name='x координата')  # minimum: 0; maximum: 3840
    y = models.IntegerField(verbose_name='y координата')  # minimum: 0; maximum: 2160


class GpsCoord(models.Model):
    latitude = models.FloatField(verbose_name='Шиирота. В градусах.')
    longitude = models.FloatField(verbose_name='Долгота. В градусах.')


class Zone(models.Model):
    """Зона обзора"""
    location = models.ForeignKey()
    address = models.CharField(verbose_name='Адрес зоны обзора', max_length=512)
    vrpDetectionArea = models.ForeignKey(Point, on_delete=models.CASCADE)


class Detector(models.Model):  # Надо сделать минимальную длину(validator)
    serialNumber = models.CharField(verbose_name='Серийный номер', max_length=50)  # , min_length=6
    model = models.CharField(verbose_name='Производитель', max_length=50)  # , min_length=1
    address = models.CharField(verbose_name='Адрес установки', max_length=512)
    location = models.ForeignKey()
    zone = models.ForeignKey()
    STATES = ('NEW', 'SETUP', 'ACTIVE')
    state = models.CharField(verbose_name='Режим работы детектора', choices=STATES)
