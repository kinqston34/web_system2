from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,"HRM/index.html")

def login(request):
    if request.method == "POST":
        return redirect("HRM:index") 
    return render(request,"HRM/login.html")

def logout(request):
    return redirect("HRM:login")

#========員工管理=========#
def employee(request):      
    return render(request,"HRM/employee.html")

def new_employee(request):     #員工入職
    return render(request,"HRM/employee_extend.html",{"view":"new_employee"})

def search_employee(request):    #員工查詢

    if request.method == "POST":
        mode = request.POST.get("mode")
        print(mode)
    return render(request,"HRM/employee_extend.html",{"view":"search_employee"})

def staff(request):            #在職員工
    ref = {"view":"staff"}
    if "base" in request.path_info:
        ref["function"] = "base"
    elif "balance" in request.path_info:    #員工餘額管理
        ref["function"] = "balance"
    elif "order_requirement" in request.path_info:  #訂餐需求管理
        ref["function"] = "order_requirement"
    
    return render(request,"HRM/employee_extend.html",ref)

def resign(request):           #離職員工
    return render(request,"HRM/employee_extend.html",{"view":"resign"})

