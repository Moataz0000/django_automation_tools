from django.db import models




class List(models.Model):
    email_list = models.CharField(max_length=50, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self) -> str:
        return self.email_list




class Subscriber(models.Model):
    email_list    = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self) -> str:
        return self.email_address    
    
    


class Email(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body    = models.TextField(max_length=2500)
    attachment = models.FileField(upload_to='email_attachments/', blank=True, null=True)   
    sent_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['sent_at']
    
    def __str__(self) -> str:
        return self.subject 