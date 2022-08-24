from django.http import HttpResponse

def home_view(*args, **kwargs):
    return HttpResponse('Hello World')