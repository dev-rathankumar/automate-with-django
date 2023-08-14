from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name
    
class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    retirement = models.DecimalField(max_digits=10, decimal_places=2)
    other_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee_name+' - '+self.designation