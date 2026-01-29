from django.db import models
from core.models import Student

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    occupied = models.IntegerField(default=0)

    def __str__(self):
        return self.number

class Allocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} in {self.room}"