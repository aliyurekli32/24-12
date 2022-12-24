from django.shortcuts import HttpResponse

def real_home(request):
    return HttpResponse('This is main HomePage..')