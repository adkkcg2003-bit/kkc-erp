from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_id = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name