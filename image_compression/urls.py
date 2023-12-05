from django.urls import path
from . import views


urlpatterns = [
    path('compress/', views.compress, name='compress'),
]
