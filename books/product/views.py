from django.shortcuts import render
from .models import *
from product.serializer import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class AuthorPaginations(PageNumberPagination):
    page_size = 1

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPaginations


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
