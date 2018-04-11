from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import login, logout, logout_then_login, password_change_done, password_change

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('password-change/', password_change, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),

]
