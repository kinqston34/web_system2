from django.shortcuts import render,redirect,HttpResponse
from CMS.models import CMS,MaterialSupply,RawMaterial,Product,Inventory
from CMS.forms import CMSLoginForm,MaterialSupplyCreateForm,RawMaterialCreateForm,ProductCreateForm,InventoryCreateForm

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

    if request.method == "POST":
        if "new_product" in request.path_info:
            form = ProductCreateForm(request.POST)
            if form.is_valid():
                data = {}
                for field in form.cleaned_data.keys():
                    data[field] = form.cleaned_data[field]
                db_product = Product(**data)
                db_product.save()
                return render(request,"CMS/inventory.html",{"create":"success"})
            return HttpResponse("Product form_error")
        if "new_inventory" in request.path_info:
            form = InventoryCreateForm(request.POST)
            if form.is_valid():
                data = {}
                for field in form.cleaned_data.keys():
                    if field == "product_id":
                        data[field] = Product.objects.get(product_id = form.cleaned_data[field])
                    else :
                        data[field] = form.cleaned_data[field]
                db_inventory = Inventory(**data)
                db_inventory.save()
                return HttpResponse("OK")
            return HttpResponse("Inventory form_error")
                
    db_product = Product.objects.all()   
    db_inventory = Inventory.objects.all()
    return render(request,"CMS/inventory.html",{"db_product":db_product,"db_inventory":db_inventory})

def material(request):
    ref={}
    if request.method == "POST":

        if "material_supplier" in request.path_info:
            form = MaterialSupplyCreateForm(request.POST)
            if form.is_valid():
                data = {}
                for field in form.cleaned_data.keys():
                    data[field] = form.cleaned_data[field]
                db_supply = MaterialSupply(**data)
                db_supply.save()
                return HttpResponse("supplier ok")
            return HttpResponse("supplier form_error")
        
        elif "raw_material" in request.path_info:
            form = RawMaterialCreateForm(request.POST)
            if form.is_valid():
                data = {}
                for field in form.cleaned_data.keys():
                    if field == "supplier_id":
                        data[field] = MaterialSupply.objects.get(supplier_id = form.cleaned_data[field])        
                    else:
                        data[field] = form.cleaned_data[field]
                
                db_raw = RawMaterial(**data)
                db_raw.save()
                return HttpResponse("raw ok")
            return HttpResponse("raw form_error")

    if "material_supplier" in request.path_info:
        ref["material"] = "material_supplier"
    elif "raw_material" in request.path_info:
        db_supply = MaterialSupply.objects.all()
        ref["material"] = "raw_material"
        ref["db_data"] = db_supply

    return render(request,"CMS/material.html",ref)

def order(request):
    return render(request,"CMS/order.html")

def food_supply(request):
    return render(request,"CMS/food_supply.html")
