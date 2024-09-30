from django.urls import path
from . import views 

urlpatterns = [
    path('', views.news, name='news'),
    path('news_add/',views.news_add, name='news_add'),
    path('news_edit/<int:news_id>',views.news_edit, name='news_edit'),
    path('news_delete/<int:news_id>', views.news_delete, name='news_delete'),
]
