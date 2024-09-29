from django.urls import path
from . import views 

urlpatterns = [
    path('', views.news, name='news'),
    path('news_edit/<int:news_id>',views.news_edit, name='news_edit')
]
