from django.urls import path

from cart.views import cart_detail

urlpatterns = [
    path('',cart_detail,name='cart_detail'),
]