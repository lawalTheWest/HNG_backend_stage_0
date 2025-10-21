from django.urls import path
from .views import profile_endpoint as pe

urlpatterns = [
    path('me/', pe, name='profile'),
]