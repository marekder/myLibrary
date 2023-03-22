from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()

# router.register('books', BookList, basename='books')
router.register('books', BookList)

urlpatterns = router.urls
