from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import send_email_task


def home(request):
    return render(request, 'home.html')




def celery(request):
    send_email_task.delay()
    return HttpResponse("<h1>Fun esecuted Success</h1>")