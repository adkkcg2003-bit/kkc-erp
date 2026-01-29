from django.db import models
from core.models import Student

class Bus(models.Model):
    route = models.CharField(max_length=100)
    number = models.CharField(max_length=20, unique=True)
    driver = models.CharField(max_length=100)
    capacity = models.IntegerField()
    students_assigned = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.number} - {self.route}"