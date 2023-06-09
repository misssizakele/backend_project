from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    page_count = models.IntegerField(default=0)
    isbn = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title