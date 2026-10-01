# from django.shortcuts import render
# from django.http import HttpResponse
# from myday.models import Product
# # Create your views here.
# def createproduct(request):   #create record (C of CRUD)
#     p_name = "Macbook"
#     p_price = 900000
#     p_offer = "10%"
#     pro = Product(p_name = p_name, p_price = p_price, p_offer = p_offer)
#     pro.save()
#     return HttpResponse("<h1>Product save Successfully!</h1>")

# def productlist(request):  #read data records (R of CRUD)
#     Products = Product.objects.all() #it returns query set of object
#     res = render(request,'productlist.html',{'Products': Products})
#     return res

# def updateProduct(request):
#     id = 2
#     p_name = "Desktop" 
#     p_price = 560000
#     p_offer = "30%"
#     Product(id = id, p_name = p_name, p_price = p_price, p_offer = p_offer).save()
#     return HttpResponse("<h1> Product update Successfully!<h1>")

# def deleteProduct(request):
#     id = 2
#     pro = Product.objects.filter(id = id)
#     pro.delete()
#     return HttpResponse("<h1> Product delete Successfully! </h1>")

# def home(request):
#     return render(request, 'home.html')

from django.shortcuts import render, redirect
from myday.models import Product

def home(request):
    return render(request, 'home.html')

def newProductForm(request):
    return render(request, 'newproductform.html')

def createproduct(request):
    if request.method == "POST":
        p_name = request.POST['p_name']
        p_price = request.POST['p_price']
        p_offer = request.POST['p_offer']
        pro = Product(p_name=p_name, p_price=p_price, p_offer=p_offer)
        pro.save()
        return redirect('read')
    return render(request, 'newproductform.html')

def productlist(request):
    Products = Product.objects.all()
    return render(request, 'productlist.html', {'Products': Products})

def updateProductForm(request):
    id = request.GET['id']
    product = Product.objects.filter(id=id).values()
    return render(request, 'updateproductform.html', {'product': product[0]})

def updateProduct(request):
    if request.method == "POST":
        id = request.POST['id']
        p_name = request.POST['p_name']
        p_price = request.POST['p_price']
        p_offer = request.POST['p_offer']
        Product.objects.filter(id=id).update(
            p_name=p_name, p_price=p_price, p_offer=p_offer
        )
        return redirect('read')
    return redirect('read')

def deleteProduct(request):
    id = request.GET['id']
    pro = Product.objects.filter(id=id)
    pro.delete()
    return redirect('read')

