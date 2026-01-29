from django.db import models
from core.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.month}"

class Expense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:30]

class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return self.title