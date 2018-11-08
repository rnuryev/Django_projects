"""MemoryBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('subsection/<subsec_slug>/', views.post_list,  name='post_list_by_subsec'),
    path('section/<sec_slug>/', views.post_list,  name='post_list_by_sec'),
    path('section/<sec_slug>/<subsec_slug>', views.post_list,  name='post_list_by_sec_and_subsec'),
    path('author/<author>/', views.post_list,  name='post_list_by_author'),
    path('comments/<article_id>', views.add_comment, name='add_comment'),

]
