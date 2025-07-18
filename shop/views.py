from django.shortcuts import render
from. models import Order, Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    # Search Functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # Paginator
    paginator = Paginator(product_objects,6)
    page = request.GET.get('page')
    product_objects =paginator.get_page(page)

    return render(request,'shop/index.html',{"product_objects" : product_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)

    return render(request,'shop/detail.html',{'product_object' : product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        fname = request.POST.get("fname","")
        lname = request.POST.get("lname","")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip = request.POST.get("zip","")
    
        order = Order(items=items,fname=fname,lname=lname,email=email,address=address,city=city,state=state,zip=zip)
        order.save()

    return render(request,'shop/checkout.html')