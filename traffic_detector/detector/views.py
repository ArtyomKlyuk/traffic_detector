from django.shortcuts import render
from rest_framework import generics
from .models import Detector
from .serializers import *


class DetectorInitializedView(generics.CreateAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorInitializedSerializer


class DetectorActiveView(generics.UpdateAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorActiveSerializer


class DetectorResetView(generics.DestroyAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorResetSerializer


class DetectorSetUpView(generics.UpdateAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorSetUpSerializer
