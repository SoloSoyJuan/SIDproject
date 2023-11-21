from django.shortcuts import render, redirect
from .forms import CustomerForm
from pymongo import MongoClient

# Create your views here.


def registerCustomer(request):
    if request.method == 'GET':
        return render(request, 'registerCustomer.html', {
            'customers': CustomerForm
        })
    else:
        try:
            form = CustomerForm(request.POST)
            obj = form.save(commit=False)
            obj.save()
            return redirect('home')
        except:
            return render(request, 'registerCustomer.html',
                          {
                              'form': CustomerForm,
                              'error': "Introduce valid data"
                          })


def home(request):
    return render(request, 'home.html')


def customers(request):
    return render(request, 'customers.html')


def orders(request):
    return render(request, 'orders.html')


def products(request):
    return render(request, 'products.html')


def categories(request):
    return render(request, 'categories.html')


def render_register_person(request):
    return render(request, 'register_person.html')
