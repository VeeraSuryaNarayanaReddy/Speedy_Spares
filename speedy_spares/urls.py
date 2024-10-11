"""
URL configuration for speedy_spares project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from speedyapp1 import views
from accounts import views as accountviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/',views.process_payment,name='payment'),
    path('cart/',views.cart,name='cart'),
    path('remove_item_from_cart/<uuid:item_uid>',views.remove_item_from_cart,name='remove_item_from_cart'),
    path('add_to_cart/<product_id>',views.add_cart,name='add_to_cart'),
    path('',views.homeview,name='home'),
    path('activate/<email_token>',accountviews.activate_email),
    path('brand/',views.brandview,name='brand'),
    path('spares/<model>',views.sparesview),
    path('login/', accountviews.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', accountviews.signup_view, name='signup'),
    path('models/<brand>',views.model_view),
    path('search/', views.search_results, name='search_results'),
]
