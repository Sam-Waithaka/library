from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length=13)

    def __str__(self):
        return self.title
