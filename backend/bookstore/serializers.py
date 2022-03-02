from datetime import datetime, date

from rest_framework import serializers

from .models import Book, Author


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_year(self, value):
        year = int(value)
        if year > datetime.today().year or year < 0:
            return serializers.ValidationError('Введен некорректный год')
        return value


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
