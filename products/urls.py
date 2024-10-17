from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:product_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:product_id>/', views.delete_item, name='delete_item'),
    path('<int:product_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), # noqa
]
