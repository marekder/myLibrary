from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


# class BookList(APIView):
#     @action(detail=True, methods=['get'])
#     def get(self, request):
#         queryset = Book.objects.all()
#         a = BooksSerializer(queryset, many=True)
#         return Response(a.data)
#
#     @classmethod
#     def get_extra_actions(cls):
#         return []

class BookList(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
