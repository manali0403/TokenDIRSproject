from django.urls import path
from .views import SimpleAPI

urlpatterns = [
    path('simple/',SimpleAPI.as_view())
]