from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personalapp/home.html' )

def contact(request):
    return render (request, 'personalapp/basic.html', {'content' : ["If you would like to contact me email me at Gamingdaily@gmail.com"]})
