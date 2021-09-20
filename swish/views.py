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

def employeesmenu(request):
    books = Employee()
    books.save()
    res  = Employee.objects.all()
    return render(request, "dataView.html", {"book_list":res})
def saveform(request):
    if request.method == 'POST':
        form = Employee()
        form=Employee(eid=request.POST['eid'], ename=request.POST['ename'],econtact=request.POST['econtact'])
        form.save()
        info=Employee.objects.all()
    else:
        print("save again:")
    return render(request, "index.html",{"form_list":info})
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
