# Generated by Django 5.0.4 on 2024-04-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_publication_date_remove_book_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_images/'),
        ),
    ]
