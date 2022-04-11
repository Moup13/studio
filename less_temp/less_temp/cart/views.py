from django.shortcuts import render

# Create your views here.
from .cart import Cart
from .forms import AddToCartForm


def cart_detail(request):
    cart =Cart(request)
    form=AddToCartForm()
    context={'cart':cart,'form':form}
    return render(request,'cart_detail.html',context)