# Generated by Django 3.2.12 on 2022-03-12 05:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Процент написания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, through='bookstore.AuthorBook', to='bookstore.Author'),
        ),
    ]