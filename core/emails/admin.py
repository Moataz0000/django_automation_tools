from django.contrib import admin
from .models import List, Subscriber, Email
# Register your models here.


@admin.register(List)
class EmailListAdmin(admin.ModelAdmin):
    list_display = ['email_list', 'created_at']
    
    
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email_list', 'email_address', 'created']    
    
    
    

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sent_at', 'attachment']        