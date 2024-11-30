from django.contrib import admin
from .models import Upload



@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['file', 'model_name', 'uploaded_at']
    search_fields = ['model_name']