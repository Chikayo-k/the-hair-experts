from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:product_id>/', views.edit_item, name='edit_item'),
]