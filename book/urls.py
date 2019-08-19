from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.book, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('del_book/<book_id>', views.del_book, name='del_book'),
    path('book_detail/<book_id>', views.book_detail, name='book_detail'),
]