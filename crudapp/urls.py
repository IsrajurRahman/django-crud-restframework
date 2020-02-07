from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addbook/', views.addbook, name='addbook'),
    path('create/', views.create, name='create'),
    path('update/<book_id>', views.update, name='update'),
    path('edit/<book_id>', views.edit, name='edit'),
    path('delete/<book_id>', views.delete, name='delete'),
    path('books_api/', views.BookListAPI.as_view()),
]