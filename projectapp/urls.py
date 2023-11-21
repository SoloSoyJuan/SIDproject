from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Customers
    path('customers/', views.customers, name='customers'),
    path('customers/views/add_customer/', views.render_add_customer, name='view_add_customer'),
    path('customers/views/add_customer/add/', views.add_customer, name='add_customer'),

    # Orders
    path('orders/', views.orders, name='orders'),
    path('orders/views/add_order/', views.render_add_order, name='view_add_order'),

    # Products
    path('products/', views.products, name='products'),

    # Categories
    path('categories/', views.categories, name='categories'),
    path('categories/views/add_category/', views.render_add_category, name='view_add_category'),
    path('categories/views/add_category/add/', views.add_category, name='add_category'),
]
