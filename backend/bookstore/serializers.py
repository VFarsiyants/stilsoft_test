from datetime import datetime, date
from rest_framework import serializers
from .models import Book, Author, AuthorBook


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate(self, attrs):
        birthdate = attrs['birthdate']
        first_name = attrs['first_name']
        last_name = attrs['last_name']
        if birthdate > date.today():
            raise serializers.ValidationError('Введена некорректныя дата рождения')
        if not (first_name.isalpha() or last_name.isalpha()):
            raise serializers.ValidationError('Некорректное имя')
        return attrs


class AuthorMergeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        exclude = ['id', 'book']


class BookMergeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        exclude = ['id', 'author']


class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorMergeModelSerializer(many=True, source="authorbook_set")

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'author',
            'published_year'
        ]

    def validate_author(self, value):
        percents = 0
        for author in value:
            percents += author['percentage']
        if percents != 100:
            raise serializers.ValidationError('Сумма процентов должна быть 100')
        return value

    def validate_year(self, value):
        year = int(value)
        if year > datetime.today().year or year < 0:
            raise serializers.ValidationError('Введен некорректный год')
        return value

    def create(self, validated_data):
        book = Book.objects.create(name=validated_data['name'], published_year=validated_data['published_year'])
        for author_book in validated_data['authorbook_set']:
            AuthorBook.objects.create(book=book, **author_book)
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.published_year = validated_data['published_year']
        instance.save()
        AuthorBook.objects.all().filter(book=instance).delete()
        for author_book in validated_data['authorbook_set']:
            AuthorBook.objects.create(book=instance, **author_book)
        return instance


class AuthorDetailedModelSerializer(serializers.ModelSerializer):
    books = BookMergeModelSerializer(many=True, source="authorbook_set")

    class Meta:
        model = Author
        fields = [
            'id',
            'first_name',
            'last_name',
            'birthdate',
            'books'
        ]
