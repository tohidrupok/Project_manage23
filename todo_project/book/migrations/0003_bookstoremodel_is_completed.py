# Generated by Django 4.2.4 on 2023-08-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_bookstoremodel_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstoremodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]