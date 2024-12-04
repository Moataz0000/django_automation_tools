from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import send_email_task


def home(request):
    return render(request, 'home.html')


