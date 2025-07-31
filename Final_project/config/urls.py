"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/
    path('', product_list, name='product_list'),
    #http://127.0.0.1:8000/category/elektronika
    path('category/<slug:slug>/', product_list, name='product_by_category'),
    #http://127.0.0.1:8000/product/mylo
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    #http://127.0.0.1:8000/cart
    path('cart/', cart_detail, name='cart_detail'),
    #http://127.0.0.1:8000/cart/add/zaporochez
    path('cart/add/<slug:slug>/', cart_add, name='cart_add'),
    #http://127.0.0.1:8000/cart/remove/noutbuk
    path('cart/remove/<slug:slug>/', cart_remove, name='cart_remove'),
    #http://127.0.0.1:8000/order/create/
    path('order/create/', order_create, name='order_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
