from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def book(request):
    return render(request,'book_index.html')


def book_detail(request,book_id):
    content = "你请求的book_id：%s 不存在！" % book_id
    return HttpResponse(content)


def author_detail(request):
    author_id = request.GET.get('id')
    content = "你请求的 author_id：%s 不存在！" % author_id
    return HttpResponse(content)
