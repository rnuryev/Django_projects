from django.urls import path, include
from . import views


urlpatterns = [
    path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('unsubscribe/<user_hash>/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),

]