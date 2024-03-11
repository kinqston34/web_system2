from django.shortcuts import render,redirect
from developer.models import Developer
from developer.forms import DeveloperLoginForm,DeveloperCreateForm
# Create your views here.

def developer(request):

    return render(request,"developer/developer.html")

def login(request):
    
    if request.method == "POST":
        form = DeveloperLoginForm(request.POST)
        if form.is_valid():
            dev_id = form.cleaned_data["account"]
            password = form.cleaned_data["password"]
        
            
            return redirect("developer:developer")
    
    return render(request,"developer/login.html")

def logout(request):
    return redirect("developer:login")


def createdeveloper(request):
    
    if request.method == "POST":
        form = DeveloperCreateForm(request.POST)
        if form.is_valid():
            dev = Developer(
                dev_id = form.cleaned_data["dev_id"],
                password = form.cleaned_data["password"],
                manager = True if bool(form.cleaned_data["manager"]) else False,        
            )
            dev.save()
            return redirect("developer:developer")

    return render(request,"developer/create.html")


