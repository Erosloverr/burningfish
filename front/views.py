from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.db import connection
from django.shortcuts import render


def index(request):
    return render(request,'front_index.html')


def login(request):
    return HttpResponse("front_login_page!")


