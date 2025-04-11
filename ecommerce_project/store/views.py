from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only


#Register
@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')      

            messages.success(request, 'Account was created for '+ username )

            return redirect('login')
        
    context = {'form': form}
    return render(request, 'store/register.html', context)

#Login
@unauthenticated_user 
def loginPage(request):
  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    context = {}
    return render(request, 'store/login.html', context)

#Log out
def logoutUser(request):
    logout(request)
    return redirect('login')


#Admin Page-dashboard
@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    sellers = Seller.objects.all()

    total_customers = customers.count()
    total_sellers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context ={'orders': orders, 'customers': customers, 'sellers': sellers,'total_customers':total_customers, 'total_sellers':total_sellers,'total_orders': total_orders, 'delivered': delivered, 'pending':pending}
    return render(request, 'store/dashboard.html', context)

#Customer Dashoard
@login_required(login_url= 'login')
@allowed_users(allowed_roles=['customer'])
def customerPage(request):

    customer = Customer.objects.get(user =request.user)
    
 
    orders = customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    print(orders)

    context = {'orders': orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
   
    context = {}
    return render(request, 'store/user.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer )
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'store/account_settings.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return  render(request, 'store/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all() #grabs child object

    order_count = orders.count()  
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return  render(request, 'store/customer.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial = {'customer': customer})
    if request.method == 'POST':
       # print('Printing POST: ', request.POST)
       #form = OrderForm(request.POST)
       formset = OrderFormSet(request.POST,instance=customer)
       if formset.is_valid():
           formset.save()
           return redirect('/')
    
    context = {'formset': formset}

    return render(request, 'store/order_formset.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) 

    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {'form': form}
    return render(request, 'store/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'store/delete.html', context)


def store(request):

    customer = Customer.objects.get(user = request.user)
    products = Product.objects.all()
    context = {'customer': customer, 'products': products}
    return render(request, 'store/store.html', context)

def item(request, pk):
    product = Product.get(id=pk)
    context ={'product':product}
    return render(request, 'store/item.html',context)
def sellerdashboard(request):
    context ={}
    return render(request, 'store/sellerdashboard.html', context)