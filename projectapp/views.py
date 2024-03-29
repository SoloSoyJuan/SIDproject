from django.shortcuts import render, redirect
from .models import CUSTOMERS
from .forms import CustomerForm

# Create your views here.

def registerCustomer(request):
    
    if request.method == 'GET':
        return render(request, 'registerCustomer.html', {
            'customers':CustomerForm
        })
    else:
        try:
            form = CustomerForm(request.POST)
            obj= form.save(commit=False)
            obj.save
            return redirect('home')
        except:
            return render(request, 'registerCustomer.html',
                  {
                      'form':CustomerForm,
                      'error': "Introduce valid data"
                  })
        
def home(request):
    return render(request, 'home.html')
    