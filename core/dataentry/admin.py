from django.contrib import admin
from .models import Student, CSVDate, Employee


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(CSVDate)
class CSVDateAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass