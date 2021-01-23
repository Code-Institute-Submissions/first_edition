from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path(
        'product_bestsellers', views.product_bestsellers, name="product_bestsellers"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_product, name='add_product'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('view_comments/<int:product_id>/', views.view_comments, name='view_comments'),
    path('edit_comment/<int:product_id>/', views.edit_comment, name='edit_comment'),
    path(
        'delete_comment/<int:product_id>/', views.delete_comment, name='delete_comment'),
    path('rate_product/<int:product_id>/', views.rate, name='rate'),

    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', (
        views.delete_product), name='delete_product'),
]
