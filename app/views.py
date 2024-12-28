from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.


def department(request):
    DTO = Department.objects.all()
    d={'DTO':DTO}
    return render(request,'department.html',d)

def employee(request):
    ETO = Employee.objects.all()
    d={'ETO':ETO}
    return render(request,'employee.html',d)