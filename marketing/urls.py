from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscribe_view, name='subscribe'),
    path('success/', views.subscribe_success, name='subscribe-success'),
    path('fail/', views.subscribe_fail, name='subscribe-fail'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('unsubscribe/success/', views.unsubscribe_success, name='unsubscribe-success'),
    path('unsubscribe/fail/', views.unsubscribe_fail, name='unsubscribe-fail'),
]