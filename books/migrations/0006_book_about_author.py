# Generated by Django 4.0.6 on 2022-07-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_alter_book_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="about_author",
            field=models.TextField(blank=True),
        ),
    ]
