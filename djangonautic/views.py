
from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return render(request,'about.html')

def homePage(request):
    return render(request,'homepage.html')
