from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Sifter 1,2,3")