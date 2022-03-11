import json

from django.conf import settings
from django.core.management import BaseCommand
from bookstore.models import Author, Book
from django.contrib.auth.models import Group, Permission, User


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        authors = load_from_json('authors')
        books = load_from_json('books')
        User.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
        Group.objects.all().delete()

        staff_rights = ['view_author', 'add_author', 'change_author',
                        'view_book', 'add_book', 'change_book']
        visitor_rights = ['view_author',
                          'view_book']

        User.objects.create_superuser(
            username='admin',
            first_name='Администратор',
            last_name='Администратор',
            email='admin@mac.local',
            password='admin'
        )

        User.objects.create_user(
            username='visitor',
            first_name='Посетитель',
            last_name='Посетитель',
            email='visitor@mac.local',
            password='visitor',
        )

        User.objects.create_user(
            username='staff',
            first_name='Персонал',
            last_name='Персонал',
            email='visitor@mac.local',
            password='staff',
            is_staff=True
        )

        User.objects.create_user(
            username='without_perm',
            first_name='Без',
            last_name='Прав',
            email='norights@mac.local',
            password='without_perm'
        )

        visitors_group = Group.objects.create(name='Посетители')
        staff_group = Group.objects.create(name='Персонал')

        User.objects.get(username='visitor').groups.add(visitors_group)
        User.objects.get(username='staff').groups.add(staff_group)

        for right in visitor_rights:
            visitors_group.permissions.add(Permission.objects.get(codename=right))

        for right in staff_rights:
            staff_group.permissions.add(Permission.objects.get(codename=right))

        for author in authors:
            Author.objects.create(**author)

        for book in books:
            author = Author.objects.get(pk=book['author'])
            Book.objects.create(id=book['id'], author=author, name=book['name'],
                                published_year=book['published_year'])
