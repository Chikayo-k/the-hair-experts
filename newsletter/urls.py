from django.urls import path

from . import views


urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('', views.subscribe, name='newsletter'),
    path('success/', views.subscribe_success, name='subscribe-success'),
    path('fail/', views.subscribe_fail, name='subscribe-fail'),
]
