from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Create your views here.
# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer_class = BooksSerializer(queryset, many=True)
#         return Response(serializer_class.data)

class BookList(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
