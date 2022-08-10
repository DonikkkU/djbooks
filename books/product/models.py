from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return f'{self.first_name, self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')