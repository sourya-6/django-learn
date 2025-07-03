from django.http  import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hey these is About Page")

def contact(request):
    return HttpResponse("Hey these is Contact Page")