from django.shortcuts import HttpResponse

def real_home(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/admin">This is admin link</a><a href="http://127.0.0.1:8000/path">This is path link</a><a href="http://127.0.0.1:8000/api">This is api link</a>')