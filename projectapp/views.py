from django.shortcuts import render, redirect
from .models import CategoryProduct, Customers, Orders
from pymongo import MongoClient


def create_customer_document(cid, fname, lname, address, dob, email, hphone, cphone):
    client = MongoClient('localhost', 27017)
    db = client['Parcial3']
    collection = db['test']
    document = Customers(customerId=cid, firstName=fname, lastName=lname, address=address,
                         dateOfBirth=dob, email=email, homePhone=hphone, cellPhone=cphone)
    prepared_doc = document.__dict__
    prepared_doc.pop('_state')
    collection.insert_one(prepared_doc)
    client.close()


def home(request):
    all_customers = Customers.objects.all()
    all_orders = Orders.objects.all()
    return render(request, 'home.html', {
        'my_customers': all_customers,
        'my_orders': all_orders,
    })


def customers(request):
    all_customers = Customers.objects.all()
    return render(request, 'customers.html', {
        'my_customers': all_customers
    })


def render_add_customer(request):
    return render(request, 'add_customer.html')


def add_customer(request):
    if request.method == 'POST':
        customer_id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        homephone = request.POST['home_phone']
        cellphone = request.POST['cellphone']
        create_customer_document(customer_id, first_name, last_name, address, date_of_birth,
                                 email, homephone, cellphone)
        Customers.objects.create(customerId=customer_id, firstName=first_name, lastName=last_name,
                                 address=address, dateOfBirth=date_of_birth, email=email,
                                 homePhone=homephone, cellPhone=cellphone)
        return redirect('customers')


def orders(request):
    all_orders = Orders.objects.all()
    return render(request, 'orders.html', {
        'my_orders': all_orders
    })


def render_add_order(request):
    all_customers = Customers.objects.all()
    return render(request, 'add_order.html', {
        'my_customers': all_customers
    })


def products(request):
    return render(request, 'products.html')


def categories(request):
    categories_p = CategoryProduct.objects.all()
    return render(request, 'categories.html', {
        'categories': categories_p
    })


def render_add_category(request):
    return render(request, 'add_category.html')


def add_category(request):
    if request.method == 'POST':
        code = request.POST['code']
        description = request.POST['description']
        CategoryProduct.objects.create(code=code, description=description)
        return redirect('categories')


def render_register_person(request):
    return render(request, 'register_person.html')
