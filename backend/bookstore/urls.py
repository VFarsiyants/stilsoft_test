from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookstore.views import BookModelViewSet, AuthorModelViewSet, AuthorDetailedModelViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('books', BookModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('authors_detailed', AuthorDetailedModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls'))
]
