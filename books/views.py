from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BooksSerializer
from rest_framework.response import Response


# Create your views here.
class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BooksSerializer
        return Response(serializer.queryset)
