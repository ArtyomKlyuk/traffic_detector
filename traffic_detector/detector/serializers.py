from rest_framework import serializers
from .models import Detector


class DetectorInitializedSerializer(serializers.Serializer):
    class Meta:
        model = Detector
        fields = ('serialNumber', 'model', 'conformityCertificate')


class DetectorActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('address_setup', 'gps_coord_device', 'zone', 'address', 'vrpDetectionArea')


class DetectorResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('__all__')


class DetectorSetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('state')
