from django.http  import HttpResponse
from django.shortcuts import render

def home(request):
    dp = request.GET.get('sourya')
    return render(request,'website/index.html',{'dp':dp})

def about(request):
    return HttpResponse("Hey these is About Page")

def contact(request):
    return HttpResponse("Hey these is Contact Page")

# def services(request):
#     dp = request.GET.get('sourya')
#     return render(request, 'layout.html', {'dp': dp})