from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('categories/views/add_category', views.render_add_category, name='view_add_category'),
    path('categories/views/add_category/add', views.add_category, name='add_category'),
    path('registerCustomer/', views.registerCustomer, name='registerCustomers'),
]
