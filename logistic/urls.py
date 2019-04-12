from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('denis/', views.denis, name = 'denis task'),
    path('vlad/', views.vladislav, name = 'vladislav task'),
]
