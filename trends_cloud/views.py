from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    context = {}
    return render(request, 'trends_cloud/main.html', context)

