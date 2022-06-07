from rest_framework import serializers
from .models import Detector, ConformityCertificate


class DetectorInitializedSerializer(serializers.ModelSerializer):
    conformityCertificate = serializers.SlugRelatedField(slug_field="certificate",
                                                         queryset=ConformityCertificate.objects.all())

    class Meta:
        model = Detector
        fields = (
            'serialNumber',
            'model',
            'conformityCertificate'
        )


class DetectorActiveSerializer(serializers.ModelSerializer):


    class Meta:
        model = Detector
        fields = (
            'address',
            'gps_coord_device',
            'zone',
            'address',
            'vrpDetectionArea')


class DetectorResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('__all__')


class DetectorSetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('state')
