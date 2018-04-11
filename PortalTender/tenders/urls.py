from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.rzd_tenders_query, name='rzd_tenders_query'),
    # path('rzd/new/', views.rzd_tenders_new, name='rzd_tenders_new'),
    path('rzd/all/', views.rzd_tenders_found, name='rzd_tenders_found'),

]
