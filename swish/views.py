from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import redirect


def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/redirect/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
"""def emp(request):
    if request.method == "POST":

    else:
        info = Employee.objects.all()
        #bookdata = {"details": info}
        #form = EmployeeForm()
        info.save()
    return render(request,{"book_list":res})"""
'''def employeesmenu(request):
    books = Employee()
    books.save()
    res  = Employee.objects.all()
    return render(request, "dataView.html", {"book_list":res})'''
def saveform(request):
    form=Employee()
    form.save()
    info=Employee.objects.all()
    return render(request, "dataView.html",{"form_list":info})

    if request.method == 'POST':
        if request.POST["id"] =="":
            form=Employee(eid=request.POST['eid'], ename=request.POST['ename'],econtact=request.POST['econtact'])
            form.save()
        elif request.POST["id"]!="":
            formdb=getEmployee(int(request.POST["id"]))
            formdb.econtact=request.POST["econtact"]
            formdb.ename=request.POST["ename"]
            formdb.eid=request.POST["eid"]
            formdb.save()
    else:
        print("save again:")
    return emp(request)
def editdetails(request,econtact):
    return render(request,"index.html", {"book":getEmployee(econtact)})
def getEmployee(id):
    formList = Employee.objects.filter(id=id)
    form = Employee()
    for x in formList:
        form=x
        break
    return form
def edit(request,econtact):
    return render(request,"index.html", {"form":getEmployee(econtact)})
