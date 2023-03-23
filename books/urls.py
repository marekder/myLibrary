from rest_framework.routers import DefaultRouter
from .views import BookList, BookDetail
from django.urls import path

# router = DefaultRouter()
#
# router.register(r'books', BookList.as_view({'get': 'get'}), basename='book_list')
# # router.register('books', BookList)
#

# router = DefaultRouter()
# router.register(r'books', BookList, basename='books')
#
# urlpatterns = router.urls

urlpatterns = [path('books/', BookList.as_view(), name='books'),
               path('books/<int:pk>/', BookDetail.as_view(), name='detail_book'), ]
