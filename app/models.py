from django.db import models

# Create your models here.

class Department(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dept_name=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)


class Employee(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=100)
    Emp_job=models.CharField(max_length=100)
    Emp_hiredate=models.DateField(auto_now=True)
    Emp_salary=models.DecimalField(max_digits=10,decimal_places=2)
    Emp_commission=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    Emp_mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    Dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
