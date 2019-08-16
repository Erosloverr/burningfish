from django.http import HttpResponse
from django.shortcuts import redirect,reverse


def index(request):
    if request.GET.get("username"):
        content = "Front_Welcome %s!" % request.GET.get("username")
        return HttpResponse(content)
    else:
        print('front')
        print(reverse('front:login'))
        return redirect(reverse('front:login'))


def login(request):
    return HttpResponse("front_login_page!")