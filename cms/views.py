from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect,reverse

app_name = 'cms'


def index(request):
    return render(request,'cms_index.html')


def login(request):
    return HttpResponse("cms_login_page!")

