from django.shortcuts import render
from rest_framework import generics
from .models import DetectorInitialized
from .serializers import DetectorDetailSerializer


class DetectorInitializedView(generics.CreateAPIView):
    queryset = DetectorInitialized.objects.all()
    serializer_class = DetectorDetailSerializer

# Create your views here.

