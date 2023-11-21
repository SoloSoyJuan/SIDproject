from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('registerCustomer/', views.registerCustomer, name='registerCustomers'),
]
