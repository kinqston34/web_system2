from django.shortcuts import render,redirect,HttpResponse
from HRM.models import Staff,HR
from HRM.forms import HRForm,StaffForm,HRMLoginFrom
# Create your views here.

def login(request):

    if request.method == "POST":
        
        form = HRMLoginFrom(request.POST)
        # print(form.data,form.errors)
        if form.is_valid():
            return redirect("HRM:employee") 
        return redirect("HRM:login")
    return render(request,"HRM/login.html")

def logout(request):
    return redirect("HRM:login")

#========員工管理=========#
def employee(request):  

    return render(request,"HRM/employee.html")

def new_employee(request):     #員工入職

    if request.method == "POST":  #POST
        if "HR_create" in request.path_info:  #HR 新增管理系統帳號
            form = HRForm(request.POST)
            if form.is_valid():    
                hr_id = form.cleaned_data["hr_id"]
                password = form.cleaned_data["password"]
                manager = form.cleaned_data["manager"]
                # print(hr_id,password,bool(manager))
                db_HR = HR(hr_id,password,bool(manager))
                db_HR.save()
                return HttpResponse("OK")
            else:
                return HttpResponse("表單error")
        
        else:
            form = StaffForm(request.POST)
            if form.is_valid():
                staff_id = form.cleaned_data["staff_id"]
                name = form.cleaned_data["name"]
                en_name = form.cleaned_data["en_name"]
                departments = form.cleaned_data["departments"]
                level = form.cleaned_data["level"]
                db_Staff = Staff(staff_id,name,en_name,departments,level)
                db_Staff.save()
                return HttpResponse("OK")
            else:
                return HttpResponse("表單error")

    ref = {"view":"new_employee","departments":{"Chair":"董事長","Pres":"總經理","HR":"人事部","IT":"資訊部","ED":"工程部"},"level":{"M":"主管","S":"一般職員"}}      #GET 
    if "HR_create" in request.path_info:
        ref["function"] = "HR_create"

    return render(request,"HRM/employee_extend.html",ref)

def search_employee(request):    #員工查詢
    ref = {"view":"search_employee"}
    if request.method == "POST":
        mode = request.POST.get("mode")
        print(mode)
        if mode == "name":
            ref["query"] = "name"
            request.session["mode"] = "name"
        elif mode == "id":    
            ref["query"] = "id"
            request.session["mode"] = "id"

    return render(request,"HRM/employee_extend.html",ref)

def search_employee_db(request):
    ref = {"view":"search_employee"}
    if request.method == "POST" and "mode" in request.session:
        mode = request.session["mode"]
        if mode == "name":
            name = request.POST["name"]
            try:
                query_data = Staff.objects.get(name = name)
                
            except:
                query_data = "no"
            
            ref["result"] = query_data
        elif mode == "id":
            id = request.POST["id"]
            try:
                query_data = Staff.objects.get(staff_id = id)
                
            except:
                query_data = "no"

            ref["result"] = query_data
        else:
            print("no thie mode")
        print(ref["result"])
        return render(request,"HRM/employee_extend.html",ref)     

def staff(request):            #在職員工

    ref = {"view":"staff"}
    if "base" in request.path_info:    # 基本資料修改
        ref["function"] = "base"
    elif "balance" in request.path_info:    #員工餘額管理
        ref["function"] = "balance"
    elif "order_requirement" in request.path_info:  #訂餐需求管理
        ref["function"] = "order_requirement"
    
    return render(request,"HRM/employee_extend.html",ref)

def resign(request):           #離職員工





    return render(request,"HRM/employee_extend.html",{"view":"resign"})


    




        





