from django.urls import path
from .api.api import api

urlpatterns = [
    path('teste/', api.urls)
]
