# Generated by Django 4.0.6 on 2022-07-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_book_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
