from django.contrib import admin
from .models import Expense, Payroll, Task

admin.site.register(Expense)
admin.site.register(Payroll)
admin.site.register(Task)