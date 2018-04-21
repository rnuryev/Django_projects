from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.rzd_tenders_query, name='rzd_tenders_query'),
    # path('rzd/new/', views.rzd_tenders_new, name='rzd_tenders_new'),
    path('', views.dashboard, name='dashboard'),
    path('favorites', views.favorites, name='favorites'),
    path('rzd/all/', views.rzd_tenders_found, name='rzd_tenders_found'),
    path('rzd/<int:pk>/', views.tender_detail, name='tender_detail'),
    path('add_remove_favorite/<int:pk>/', views.add_remove_favorite, name='add_remove_favorite'),
    path('in_favorite/<int:pk>/', views.in_favorite, name='in_favorite'),

]
