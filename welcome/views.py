import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    return render(request, 'personalapp/home.html' )

def contact(request):
    return render (request, 'personalapp/basic.html', {'content' : ["If you would like to contact me email me at Gamingdaily@gmail.com"]})



#def index(request):
  #  hostname = os.getenv('HOSTNAME', 'unknown')
   # PageView.objects.create(hostname=hostname)

    #return render(request, 'welcome/index.html', {
     #   'hostname': hostname,
      #  'database': database.info(),
       # 'count': PageView.objects.count()
   # })

def health(request):
    return HttpResponse(PageView.objects.count())
