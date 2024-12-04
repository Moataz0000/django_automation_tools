from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from dataentry.utils import send_email_notification
from django.conf import settings
from .models import Subscriber
from .tasks import send_list_email_task




def send_email(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST, request.FILES)
        if email_form.is_valid():
            email_form = email_form.save()
            # send an email
            mail_subject = request.POST.get('subject')
            message      = request.POST.get('body')
            email_list = request.POST.get('email_list')

            
            # access the selected email list
            email_list = email_form.email_list
            
            # extrac email addressess from subscriber model in the selected email list
            subscribers = Subscriber.objects.filter(email_list=email_list)
            
            to_email = [email.email_address for email in subscribers]   
            # send a list of email with celery task
            if email_form.attachment:
                attachment = email_form.attachment.path
            else:
                attachment = None
            send_list_email_task.delay(mail_subject, message, to_email, attachment)

            
            # Display a success message
            messages.success(request, 'E-mail sent successfully.')
            return redirect('emails:send_email')
    else:
        form = EmailForm
    context = {
        'form': form
    }    
    return render(request, 'emails/send_email.html', context)