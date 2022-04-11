from django.urls import path
from .views import get_first_page,createProduct
urlpatterns = [
    # path('',get_first_page,name='first_page'),
    path('create/',createProduct,name='create'),
]
