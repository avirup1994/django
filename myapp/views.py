from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def myapp(request):
    return render(request,'myapp/myapp.html')