from django.contrib import admin
from .models import Student, CSVDate


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(CSVDate)
class CSVDateAdmin(admin.ModelAdmin):
    pass
