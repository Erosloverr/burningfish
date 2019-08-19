from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.book, name='index'),
    path('book_detail/<book_id>', views.book_detail, name='book_detail'),
    path('author_detail/', views.author_detail, name='author_detail'),
]