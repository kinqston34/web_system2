from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,"CMS/index.html")

def login(request):

    if request.method == "POST":
        return redirect("CMS:index")    
    return render(request,"CMS/login.html")

def logout(request):
    return redirect("CMS:login")

def inventory(request):
    return render(request,"CMS/inventory.html")

def material_supply(request):
    return render(request,"CMS/material_supply.html")

def order(request):
    return render(request,"CMS/order.html")

def HR(request):
    return render(request,"CMS/HR.html")

def food_supply(request):
    return render(request,"CMS/food_supply.html")
