from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()

router.register(r'books', BookList, basename='book_list')
# router.register('books', BookList)

urlpatterns = router.urls
