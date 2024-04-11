from django.shortcuts import render,redirect,HttpResponse
from CMS.models import CMS,MaterialSupply,RawMaterial
from CMS.forms import CMSLoginForm,MaterialSupplyCreateForm,RawMaterialCreateForm

# Create your views here.

def index(request):
    return render(request,"CMS/index.html")

def login(request):

    if request.method == "POST":
        form = CMSLoginForm(request.POST)
        if form.is_valid():
            return redirect("CMS:index")    
        return redirect("CMS:login")
    return render(request,"CMS/login.html")

def logout(request):
    return redirect("CMS:login")

def inventory(request):
    return render(request,"CMS/inventory.html")

def material(request):
    ref={}
    if request.method == "POST":

        if "material_supplier" in request.path_info:
            form = MaterialSupplyCreateForm(request.POST)
            if form.is_valid():
                fields = ["supplier_id","name","address","tel","salesman","salesman_phone"]
                data = {}
                for field in fields:
                    data[field] = form.cleaned_data[field]
                db_supply = MaterialSupply(**data)
                db_supply.save()
                return HttpResponse("supplier ok")
            return HttpResponse("supplier form_error")
        elif "raw_material" in request.path_info:
            form = RawMaterialCreateForm(request.POST)
            if form.is_valid():
                fields = ["material_id","name","category"]
                data = {}
                for field in fields:
                    data[field] = form.cleaned_data[field]
                db_supply = RawMaterial(**data)
                db_supply.save()
                return HttpResponse("raw ok")
            return HttpResponse("raw form_error")

    if "material_supplier" in request.path_info:
        ref["material"] = "material_supplier"
    elif "raw_material" in request.path_info:
        ref["material"] = "raw_material"

    return render(request,"CMS/material.html",ref)

def order(request):
    return render(request,"CMS/order.html")

def food_supply(request):
    return render(request,"CMS/food_supply.html")
