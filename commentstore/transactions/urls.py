from django.urls import path
from . import views

urlpatterns = [
    path('', views.points_transfer, name='pointstransfer'),
    path('points/', views.points_view, name='points'),
]