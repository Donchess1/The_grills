from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.timetable, name='menu'),
    path('review/', views.review, name='review'),
    path('signup/', views.signup, name='signup'),
]
