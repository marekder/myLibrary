from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


class BookList(APIView):
    @action(detail=True, methods=['get'])
    def get(self, request):
        queryset = Book.objects.all()
        a = BooksSerializer(queryset, many=True)
        return Response(a.data)

    def post(self, request):
        a = BooksSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        return Response(a.errors)


class BookDetail(APIView):
    def get(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        a = BooksSerializer(queryset)
        return Response(a.data)

    def delete(self, request, pk):
        queryset = get_object_or_404(Book, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        print(queryset)
        data = request.data

        return Response()

        # a = BooksSerializer(data=request.data)
        # if a.is_valid():
        #     a.save()
        #     return Response(a.data)
        # return Response(a.errors)

    # @classmethod
    # def get_extra_actions(cls):
    #     return []

# class BookList(APIView):
#     @action(detail=True, methods=['get'])
#     def get(self, request):
#         queryset = Book.objects.all()
#         a = BooksSerializer(queryset, many=True)
#         return Response(a.data)
#
#     #
#     @classmethod
#     def get_extra_actions(cls):
#         return []

# class BookList(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer
