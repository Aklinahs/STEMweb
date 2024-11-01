from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello, This is our first custom page.")