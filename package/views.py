# from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    # return HttpResponse("This is HomePage")
    return render(request, 'home.html')

def About(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')
