# Generated by Django 2.2.10 on 2020-07-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
