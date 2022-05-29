from django.contrib import admin
from django.urls import path, include
from .views import DetectorInitializedView


urlpatterns = [
    path('initialized/', DetectorInitializedView.as_view())
]
