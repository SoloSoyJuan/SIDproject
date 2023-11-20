from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerCustomer/', views.registerCustomer, name='registerCustomers'),
    path('view_register_person/', views.render_register_person, name='render_register_person'),
    path('register_person/', views.register_person, name='register_person'),
]
