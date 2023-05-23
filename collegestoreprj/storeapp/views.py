from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Product
# from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def dept(request,c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Department, slug=c_slug)
        products_list = Product.objects.all().filter(department=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request,"department.html", {'department':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(department__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def new(request):
    return render(request,'new.html')

def order(request):
    return render(request,'order.html')

def logout(request):
    return render(request,'login.html')

def confirm(request):
    return render(request,'confirm.html')