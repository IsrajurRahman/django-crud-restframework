from django.shortcuts import render, redirect
from .models import BookList

# For api
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import booklistSerializer

def index(request):
    books = BookList.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'crudproject/index.html', context)

def addbook(request):
    return render(request, 'crudproject/addBook.html')

def create(request):
    name = request.GET['bookName']
    price = request.GET['bookPrice']
    author = request.GET['bookAuthor']
    book_details = BookList(name=name, price=price, author=author)
    book_details.save()

    return redirect('index')

def delete(request, book_id):
    book = BookList.objects.get(pk=book_id)
    book.delete()
    return redirect('index')

def edit(request, book_id):
    book = BookList.objects.get(pk=book_id)
    context = {
        'book':book
    }
    return render(request, 'crudproject/editbook.html', context)

def update(request, book_id):
    book = BookList.objects.get(pk=book_id)
    name = request.GET['bookName']
    price = request.GET['bookPrice']
    author = request.GET['bookAuthor']
    book_detail = BookList(name=name, price=price, author=author)
    book_detail.save()

    return redirect('index')


class BookListAPI(APIView):

    def get(self, request):
        books = BookList.objects.all()
        serializer=booklistSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
