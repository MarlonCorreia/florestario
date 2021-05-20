from django.db import models
from author.models import Author

# Create your models here.
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.TextField(max_length=100)
    summary = models.TextField(max_length=200)
    first_paragraph = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title