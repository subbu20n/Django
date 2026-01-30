from django.db import models

# Create your models here. 
# -----creating a table -------

class  userprofile(models.Model): 
    name=models.CharField(max_length=150)  
    age=models.IntegerField() 
    city=models.CharField(max_length=150)

class Employee(models.Model): 
    emp_name=models.CharField(max_length=150)
    emp_salary=models.IntegerField()
    emp_email=models.EmailField(unique=True)