from django.urls import path
from . import views


urlpatterns = [
    path('send-email/', views.send_email, name='send_email'),
    path('track/click/<unique_id>/', views.track_click, name='track_click'),
    path('track/open/<unique_id>/', views.track_open, name='track_open'),
    path('track/dashboard/', views.track_dashboard, name='track_dashboard'),
    path('track/stats/<int:pk>/', views.track_stats, name='track_stats'),
]
