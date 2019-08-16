from django.http import HttpResponse
from django.shortcuts import redirect,reverse

app_name = 'cms'

def index(request):
    if request.GET.get("username"):
        content = "CMS_Welcome %s!" % request.GET.get("username")
        return HttpResponse(content)
    else:
        print('cms')
        print(reverse('cms:login'))
        return redirect(reverse('cms:login'))


def login(request):
    return HttpResponse("cms_login_page!")

