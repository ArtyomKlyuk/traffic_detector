from rest_framework import serializers
from .models import DetectorInitialized


class DetectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectorInitialized
        fields = ('__all__')
