from django_filters import rest_framework as filters

from bookstore.models import Book


class BookFilter(filters.FilterSet):
    author__first_name = filters.CharFilter(lookup_expr='contains', label='Имя автора содержит')
    author__last_name = filters.CharFilter(lookup_expr='contains', label='Фамилия автора содержит')
    name = filters.CharFilter(lookup_expr='contains', label='Название книги содержит')
    published_year_gte = filters.NumberFilter(field_name='published_year', lookup_expr='gte',
                                              label='Год издания после')
    published_year_lte = filters.NumberFilter(field_name='published_year', lookup_expr='lte',
                                              label='Год издания до')


class AuthorFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='contains')
    last_name = filters.CharFilter(lookup_expr='contains')
    birthdate_gte = filters.DateFilter(field_name='birthdate', lookup_expr='gte', label='Родился после')
    birthdate_lte = filters.DateFilter(field_name='birthdate', lookup_expr='lte', label='Родился до')
