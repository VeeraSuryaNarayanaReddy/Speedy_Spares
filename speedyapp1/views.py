from django.shortcuts import render
import csv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import *
from django.http import HttpResponseRedirect
from instamojo_wrapper import Instamojo
from django.conf import settings

api = Instamojo(api_key=settings.INSTAMOJO_API_KEY,
                    auth_token=settings.INSTAMOJO_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')
def process_payment(request):
    cart = Cart.objects.get(is_paid=False, user=request.user)
    total_amount = cart.get_cart_total()
    print(total_amount)

    response = api.payment_request_create(
        amount=total_amount,
        purpose="Orders",
        email="rnarayana183@gmail.com",
        send_email=True,
        buyer_name=request.user.first_name,
        redirect_url="http://127.0.0.1:8000/"
    )

    # Redirect the user to the payment URL
    if response['success']:
        payment_url = response['payment_request']['longurl']
        return redirect(payment_url)  # Redirecting to Instamojo payment URL
    else:
        # Handle the case when payment request creation fails
        return redirect('error_page')  # Redirect to an error page or show a message


def logout_view(request):
    logout(request)
    # Redirect to a success page after logout
    return redirect('home')  # Replace 'home' with your desired URL name

def brandview(request):
    query_set = Brand.objects.all()
    return render(request,'brand.html',{'query_set' : query_set})


def sparesview(request,model):
    query_set = Spares.objects.filter(model__model_name=model)
    return render(request,'spares.html',{'query_set':query_set})


def model_view(request,brand):
    query_set = Brand_models.objects.filter(brand__brand_name=brand)
    return render(request,'models.html',{'query_set': query_set})


def homeview(request):
    query_set = Brand.objects.all()
    return render(request, 'home.html',{'query_set' : query_set})


@login_required
def add_cart(request, product_id):
    user = request.user
    spare_obj = Spares.objects.get(uid=product_id)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    
    # Check if the product is already in the cart
    existing_item = CartItem.objects.filter(cart=cart, products=spare_obj).first()
    if existing_item:
        # If the product is already in the cart, increase the quantity by one
        existing_item.quantity += 1
        existing_item.save()
    else:
        # If the product is not in the cart, create a new CartItem with quantity set to one
        CartItem.objects.create(
            cart=cart,
            products=spare_obj,
            quantity=1
        )
    
    return redirect('brand')
@login_required
def cart(request):
    cart,_ = Cart.objects.get_or_create(is_paid=False,user=request.user)
    for item in cart.cart_items.all():
        item.total_price = item.products.spare_price * item.quantity
    context = {'cart':cart}
    return render(request,'cart.html',context)

def remove_item_from_cart(request,item_uid):
    cart = Cart.objects.get(is_paid=False,user=request.user)
    cart_item=CartItem.objects.get(cart=cart,uid=item_uid)
    cart_item.delete()
    return redirect('cart')

def orders(request):
    orders_obj=Cart.objects.filter(user=request.user,is_paid=True)
    context={'orders_obj':orders_obj}
    return render(request,'orders.html',context)


from django.db.models import Q  # Import this for complex queries

def search_results(request):
    query = request.GET.get('query')
    
    if query:
        brand_results = Brand.objects.filter(Q(brand_name__icontains=query))
        spare_results = Spares.objects.filter(Q(spare_name__icontains=query))

        context = {
            'query': query,
            'brand_results': brand_results,
            'spare_results': spare_results
        }
    else:
        context = {
            'query': None,
            'brand_results': None,
            'spare_results': None
        }

    return render(request, 'search_results.html', context)