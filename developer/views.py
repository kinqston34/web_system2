from django.shortcuts import render,redirect,HttpResponse
from developer.models import Developer
from developer.forms import DeveloperLoginForm,DeveloperCreateForm
# Create your views here.

def developer(request):

    return render(request,"developer/developer.html")

def login(request):
    
    if request.method == "POST":
        form = DeveloperLoginForm(request.POST)
        if form.is_valid():
            
            return redirect("developer:developer")
        return redirect("developer:login")
    return render(request,"developer/login.html")

def logout(request):
    return redirect("developer:login")


def createdeveloper(request):
    
    if request.method == "POST":
        form = DeveloperCreateForm(request.POST)
        if form.is_valid():
            dev_id = form.cleaned_data["dev_id"]
            password = form.cleaned_data["password"]
            print(dev_id)
            dev = Developer(dev_id,password)
            return redirect("developer:developer") if dev.save() else HttpResponse("不是公司員工")
            

    return render(request,"developer/create.html")


