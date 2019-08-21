from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        data = "({id},{name},{author})".format(id=self.id, name=self.name, author=self.author)
        return data