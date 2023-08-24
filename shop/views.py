from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'base.html',{'products':products}) 
def home(request):
    
   
    return render(request,'home.html')