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

def employee(request):
    return render(request,"HRM/employee.html")

def new_employee(request):
    return render(request,"HRM/employee_extend.html")

def staff(request):
    return render(request,"HRM/employee_extend.html")

def food_order(request):
    return render(request,"HRM/food_order.html")