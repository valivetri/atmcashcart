from django.contrib import admin
from django.urls import path
from appname import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('count/', views.count, name='count'),
    path('process/', views.analyze, name='analyze'),
    path('final/', views.final, name='final')
]
