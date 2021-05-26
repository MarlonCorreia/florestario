from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    picture = models.URLField()

    def __str__(self):
        return self.name