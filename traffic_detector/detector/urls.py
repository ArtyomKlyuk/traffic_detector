from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('initialized/', DetectorInitializedView.as_view()),
    path('active/', DetectorActiveView.as_view()),
    path('reset/', DetectorResetView.as_view()),
    path('setup/', DetectorSetUpView.as_view()),
]
