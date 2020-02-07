from django.db import models

class BookList(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
