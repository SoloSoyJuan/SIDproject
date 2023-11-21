from django.shortcuts import render, redirect
from .models import CategoryProduct, Customer, Order, Product
from pymongo import MongoClient


def create_customer_document(cid, fname, lname, address, dob, email, hphone, cphone):
    client = MongoClient('localhost', 27017)
    db = client['Parcial3']
    collection = db['test']
    document = Customer(customerId=cid, firstName=fname, lastName=lname, address=address,
                        dateOfBirth=dob, email=email, homePhone=hphone, cellPhone=cphone)
    prepared_doc = document.__dict__
    prepared_doc.pop('_state')
    collection.insert_one(prepared_doc)
    client.close()


def home(request):
    all_customers = Customer.objects.all()
    all_orders = Order.objects.all()
    all_products = Product.objects.all()
    return render(request, 'home.html', {
        'my_customers': all_customers,
        'my_orders': all_orders,
        'my_products': all_products,
    })


def customers(request):
    all_customers = Customer.objects.all()
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
        Customer.objects.create(customerId=customer_id, firstName=first_name, lastName=last_name,
                                address=address, dateOfBirth=date_of_birth, email=email,
                                homePhone=homephone, cellPhone=cellphone)
        return redirect('customers')


def add_more_data_customer(request):
    client = MongoClient('localhost', 27017)
    db = client['Parcial3']
    my_collection = db['test']
    if request.method == 'POST':
        customer_id = request.POST['customer']
        criterio = {'customerId': customer_id}
        new_data = {
            'son': {
                'name': request.POST['full_name'],
                'date_of_birth': request.POST['dob'],
                'gender': request.POST['gender']
            },
            'place_of_birth': {
                'mun_or_ci': request.POST['mun_or_ci'],
                'dep_or_state': request.POST['dep_or_sta'],
                'country': request.POST['country']
            },
            'place_of_living':{
                'mun_or_ci': request.POST['mun_or_ci_1'],
                'dep_or_state': request.POST['dep_or_sta_1'],
                'country': request.POST['country_1'],
                'post_code':request.POST['post_code']
            },
            'hobbies': request.POST['hobbie'],
            'sports': request.POST['sport'],
            'categories':request.POST['categories'],
            'civil_status':{
                'status': request.POST['civil_status'],
                'date': request.POST['date_of_change'],
                'couple_name': request.POST['couple_name'],
                'couple_id': request.POST['couple_id']
            }
        }
        result = my_collection.update_one(criterio, {'$set': new_data})
        if result.modified_count > 0:
            print("Datos agregados correctamente al documento")
        else:
            print("No se encontró el documento o no se realizaron cambios")
        client.close()
        return redirect('customers')
    else:
        return redirect('customers')


def select_customer(request):
    if request.method == 'GET':
        all_customers = Customer.objects.all()
        return render(request, 'select_customer.html', {
            'my_customers': all_customers,
        })
    elif request.method == 'POST':
        customer_id = request.POST['customer_id']
        customer = Customer.objects.get(customerId=customer_id)
        if customer is None:
            return redirect('customers')
        else:
            return render(request, 'add_more_data_customer.html', {
                'customer_data': customer,
            })


def orders(request):
    all_orders = Order.objects.all()
    return render(request, 'orders.html', {
        'my_orders': all_orders
    })


def render_add_order(request):
    if request.method == 'GET':
        all_customers = Customer.objects.all()
        return render(request, 'add_order.html', {
            'my_customers': all_customers
        })
    elif request.method == 'POST':
        order_number = request.POST['order_id']
        customer_id = request.POST['customer_id']
        order_date = request.POST['order_date']
        shipped_date = request.POST['shipped_date']
        payment_date = request.POST['payment_date']

        customer = Customer.objects.get(customerId=customer_id)

        Order.objects.create(orderNumber=int(order_number), customerid=customer,
                             orderDate=order_date, shippedDate=shipped_date, paymentDate=payment_date)

        return redirect('orders')


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
