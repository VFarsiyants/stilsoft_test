from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    birthdate = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    author = models.ManyToManyField(Author, through='AuthorBook', blank=True)
    name = models.CharField(max_length=64, verbose_name='Название книги')
    published_year = models.IntegerField(verbose_name='Год издания')

    def __str__(self):
        return f'{self.name}'


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    percentage = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)],
                                          verbose_name="Процент написания")

    def __str__(self):
        return f'{self.author} - {self.book} - {self.percentage}'
