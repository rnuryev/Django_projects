from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.rzd_tenders_query, name='rzd_tenders_query'),
    # path('rzd/new/', views.rzd_tenders_new, name='rzd_tenders_new'),
    path('', views.dashboard, name='dashboard'),
    path('favorites', views.favorites, name='favorites'),
    path('rzd/', views.rzd_tenders_found, name='rzd_tenders_found'),
    path('rosseti/', views.rosseti_tenders_found, name='rosseti_tenders_found'),
    path('gazprom/', views.gazprom_tenders_found, name='gazprom_tenders_found'),
    path('rosatom/', views.rosatom_tenders_found, name='rosatom_tenders_found'),
    path('<int:pk>/', views.tender_detail, name='tender_detail'),
    path('add_remove_favorite/<int:pk>/', views.add_remove_favorite, name='add_remove_favorite'),
    path('in_favorite/<int:pk>/', views.in_favorite, name='in_favorite'),
    path('all/', views.all_tenders, name='all_tenders'),

]
