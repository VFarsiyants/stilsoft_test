from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .filters import BookFilter, AuthorFilter
from .models import Book, Author
from .serializers import BookModelSerializer, AuthorModelSerializer


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class BookModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all().order_by('name')
    pagination_class = BookLimitOffsetPagination
    filterset_class = BookFilter


class AuthorModelViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all().order_by('first_name')
    pagination_class = AuthorLimitOffsetPagination
    filterset_class = AuthorFilter
