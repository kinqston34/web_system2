from django.shortcuts import render,redirect,HttpResponse
from developer.models import Developer
from developer.forms import DeveloperLoginForm,DeveloperCreateForm
from CMS.forms import CMSCreateForm
from CMS.models import CMS
from HRM.forms import HRForm
from HRM.models import HR
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


def create(request):
    
    if request.method == "POST":
        if "create_developer" in request.path_info: 
            form = DeveloperCreateForm(request.POST)
            if form.is_valid():
                dev_id = form.cleaned_data["dev_id"]
                password = form.cleaned_data["password"]
                print(dev_id)
                dev = Developer(dev_id,password)
                return redirect("developer:developer") if dev.save() else HttpResponse("不是公司員工")
            
        elif "create_CMS" in request.path_info: 
            form = CMSCreateForm(request.POST)
            if form.is_valid():
                CMS_id = form.cleaned_data["CMS_id"]
                password = form.cleaned_data["password"]
                print(CMS_id)
                cms = CMS(CMS_id,password)
                return redirect("developer:developer") if cms.save() else HttpResponse("不是公司員工")

        elif "create_HRM" in request.path_info: 
            form = HRForm(request.POST)
            if form.is_valid():
                hr_id = form.cleaned_data["hr_id"]
                password = form.cleaned_data["password"]
                print(hr_id)
                hr = HR(hr_id,password)
                return redirect("developer:developer") if hr.save() else HttpResponse("不是公司員工")
    
    ref = {}
    if "create_developer" in request.path_info: 
        ref["create"] = "developer"
    elif "create_CMS" in request.path_info: 
        ref["create"] = "CMS"
    elif "create_HRM" in request.path_info: 
        ref["create"] = "HRM"

    return render(request,"developer/create.html",ref)

