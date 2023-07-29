from django.shortcuts import render,redirect
from .models import Products,Orders
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    product_objects = Products.objects.all()
    #Search Code Starts
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)
        if product_objects.exists():
            return render(request, 'shop/index.html', {'product_objects': product_objects})
        else:
            return redirect('Out_of_stock/') 
    #Search Code Ends
    #Paginator Code starts
    paginator = Paginator(product_objects, 6)#display 4 items in a page
    page = request.GET.get('page')#get the current page number from request
    product_objects = paginator.get_page(page)#get the page object from the requested page number
    return render(request,'shop/index.html',{'product_objects':product_objects})


def Out_of_stock(request):
    return render(request, 'shop/stock.html')



def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html', {'product_object': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        code = request.POST.get('code',"")
        totalquantity = request.POST.get('totalquantity',"")
        totalcost = request.POST.get('totalcost',"")

        order = Orders(items=items,name=name,email=email,address=address,city=city,code=code,totalquantity=totalquantity,totalcost=totalcost)
        order.save()

    return render(request,'shop/checkout.html') 