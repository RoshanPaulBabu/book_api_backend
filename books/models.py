from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    historical_period = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    related_books = models.ManyToManyField('self', blank=True)
    description = models.TextField(blank=True)  # New description field
    image = models.ImageField(upload_to='book_images/', blank=True)  # New image field

    def __str__(self):
        return self.title
